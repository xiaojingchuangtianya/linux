from django.contrib import admin
from django.urls import path
from .views import goods_list,good_detail
urlpatterns =[
    path("",goods_list),
    path("detail<int:good_id>",good_detail)
]


