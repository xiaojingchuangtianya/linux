from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog,Blog_type,Read_count
from comment.models import Comment
from django.contrib import auth
from my_project.forms import RegForm #注册表单
from comment.forms import CommentForms #评论表单
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def blog_list(request):
    p_num=int(request.GET.get("page",1))#获取页码
    blogs=Blog.objects.all()
    blog_type=Blog_type.objects.all()
    paginator=Paginator(blogs,8)#把所有列表分页，每页10篇
    page=paginator.get_page(p_num)
    pagination=[]
    for i in range(p_num-2,p_num+3):
        if i >0 and i<paginator.num_pages+1:
            pagination.append(i)
    last=paginator.page_range[-1]
    return render(request,"blog_list.html",context={"blogs":page.object_list,
                                                    "types":blog_type,
                                                    "page_range":pagination,
                                                    "now_page":p_num,
                                                    "previous":p_num-1,
                                                    "next":p_num+1,
                                                    "last":last})

def blog_detail(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog_content_type =ContentType.objects.get_for_model(blog)
    comment = Comment.objects.filter(content_type=blog_content_type,object_id = blog_id)

    if not request.COOKIES.get("blog"+str(blog_id)+"_read"):#读取cookies,如果存在就不增加阅读量
        if Read_count.objects.filter(blog=blog).count():
            read_num=Read_count.objects.get(blog=blog)#存在实例，获取到，再加1
        else:
            read_num=Read_count()#不存在记录，则实例化
            read_num.blog=blog
        read_num.read_num += 1
        read_num.save()
    comment_form = CommentForms(initial={"content_type": blog_content_type.model, "object_id": blog_id})
    previous_blog=Blog.objects.filter(create_time__lt=blog.create_time).first()
    next_blog=Blog.objects.filter(create_time__gt=blog.create_time).last()
    response=render(request,"blog.html",context={"blog":blog,
                                               "previous":previous_blog,
                                               "next":next_blog,
                                                "form":comment_form,
                                                "comment":comment})#响应返回
    response.set_cookie("blog"+str(blog_id)+"_read","read",max_age=86400)#设置cookie,过期时间为24小时
    return response

def types(request,type_id):
    p_num = int(request.GET.get("page", 1))  # 获取页码
    blog_type=get_object_or_404(Blog_type,id=type_id)#获取到分类的名字
    blogs=Blog.objects.filter(blog_type=blog_type)#获取到这个名字后进行filter
    paginator=Paginator(blogs,8)
    page=paginator.get_page(p_num)
    pagination = []
    for i in range(p_num - 2, p_num + 3):
        if i > 0 and i < paginator.num_pages + 1:
            pagination.append(i)
    last = paginator.page_range[-1]
    return render(request,"classify.html",context={"type_name":blog_type,
                                                   "type_id":type_id,
                                                   "type_blogs":page,
                                                   "page_blog":pagination,
                                                   "now_page": p_num,
                                                   "previous": p_num - 1,
                                                   "next": p_num + 1,
                                                   "last": last
                                                   })

def user_login(request):
    return render(request,"login.html")

def deal_login(request):
    username = request.POST["user"]
    password = request.POST["password"]

    user = authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect("./")
    else :
        #这里写一个弹窗吧
        return render(request,"error.html",context={"error":"密码错误"})

def search(request):
    return render(request,"search.html")

def log_out(request):
    redirect_url = request.META.get("HTTP_REFERER", "./")
    if request.user.is_authenticated:
        logout(request)
        return redirect(redirect_url)
    else:
        return render(request,"error.html",context={"error":"账号已经登出了"})


def registe(request):
    register_form = RegForm()#实例化form表单
    if request.method =="POST":
        register_form = RegForm(request.POST)
        if register_form.is_valid():
            username= register_form.cleaned_data["username"]
            email =register_form.cleaned_data["email"]
            password = register_form.cleaned_data["password"]
            user=User.objects.create_user(username,email,password)
            user.save()
            #实现注册完自动在线
            login_user = authenticate(username=username,password=password)
            auth.login(request,login_user)
            return redirect("/web")

    return render(request,"register.html",context={
                                                "form":register_form
                                                        })
