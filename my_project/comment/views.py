from django.shortcuts import render
from .models import Comment
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from .forms import CommentForms
# Create your views here.

def post_comment(request):
    #保存数据
    Cforms = CommentForms(request.POST,user=request.user)
    if Cforms.is_valid():
        comment = Comment()  # 实例化模型
        comment.content_object = Cforms.cleaned_data["content_obj"]
        comment.comment = Cforms.cleaned_data["comment"]
        comment.author = Cforms.cleaned_data["user"]
        comment.save()
        print("保存了一条评论！")


    old_url = request.META.get("HTTP_REFERER", "./")
    return redirect(old_url)