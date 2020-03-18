from django import forms
from django.contrib import auth
from django.contrib.auth.models import User

class RegForm(forms.Form):
    username = forms.CharField(label="账号",min_length=5,
                                max_length=20,widget=forms.TextInput(attrs={"class":"form-control",
                                                                            "placeholder":"请输入账号"}))
    email = forms.CharField(label="邮箱", widget=forms.TextInput(attrs={"class": "form-control",
                                                                             "placeholder": "请输入邮箱"}))
    password = forms.CharField(label="密码",min_length=8,
                                max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control",
                                                                            "placeholder":"请输入密码"}))
    password_again = forms.CharField(label="密码",min_length=8,
                                max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control",
                                                                            "placeholder":"请确认密码"}))
    def clean_user_name(self):
        username =self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("用户名已经存在！")
        else:
            return username

    def clean_email(self):
        email =self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("邮箱已经被注册")
        else:
            return email

    def clean_password_again(self):
        password = self.cleaned_data["password"]
        password_again =self.cleaned_data["password_again"]
        if password != password_again:
            raise forms.ValidationError("两次密码不一致")
        return password_again