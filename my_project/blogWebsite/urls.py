from django.urls import path
from . import views

urlpatterns=[
    path("",views.blog_list),
    path("blog<int:blog_id>",views.blog_detail),
    path("type<int:type_id>",views.types),
    path("search",views.search),
    path("login",views.user_login,name="web_login"),
    path("deal_login",views.deal_login),
    path("logout",views.log_out),
    path("register",views.registe,name="register"),#注册界面
]

