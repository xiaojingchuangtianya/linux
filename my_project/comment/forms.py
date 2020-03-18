from django import forms
from django.contrib.contenttypes.models import ContentType
from ckeditor.widgets import CKEditorWidget

class CommentForms(forms.Form):
    content_type =forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    comment = forms.CharField(widget=CKEditorWidget(config_name="ckeditor_comment"))

    def __init__(self,*args,**kwargs):
        if "user" in kwargs:
            self.user =kwargs.pop("user")
        super(CommentForms, self).__init__(*args,**kwargs)

    def clean(self):
        if self.user.is_authenticated:
            self.cleaned_data["user"] =self.user
        else:
            raise forms.ValidationError("用户尚未登陆")
        # 验证被评论的博客
        content_type=self.cleaned_data["content_type"]
        object_id = self.cleaned_data["object_id"]
        try:
            model_class = ContentType.objects.get(model=content_type).model_class()
            model_obj = model_class.objects.get(pk=object_id)
            self.cleaned_data["content_obj"]=model_obj
        except Exception as e:
            raise forms.ValidationError("评论的文章已经被删除了")

        return self.cleaned_data
