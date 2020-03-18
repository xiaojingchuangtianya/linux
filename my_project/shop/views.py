from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import goods

# Create your views here.
def goods_list(request):
    old_good=goods.objects.filter(classification=1)
    book = goods.objects.filter(classification=2)
    return render(request,"goods_list.html",context={"old_goods":old_good,"book":book})

def good_detail(request,good_id):
    try:
        all_good=goods.objects.get(id=good_id)
        return render(request,"good_detail.html",context={"good":all_good})
    except:
        return render(request,"error.html")