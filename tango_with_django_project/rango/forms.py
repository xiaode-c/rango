# coding:utf-8

from django import forms
from django.contrib.auth.models import User
from rango.models import Category, Page, UserProfile

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=120, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    links = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=120, help_text="Please input the title of the page")
    url = forms.URLField(max_length=200, help_text="Please input the url of the page")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category', )
    #重写ModelForm模块里clean()方法.这个方法会在表单数据存储到模型实例之前被调用,可以用来验证甚至修改用户输入的数据.
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not (url.startswith("http://") or url.startswith("https://")):
            url = 'http://' + url
            cleaned_data['url'] = url
        #必须每次都是以返回cleaned_data字典来结束clean()方法
        return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

