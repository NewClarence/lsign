# -*- coding: UTF-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from cmdb import models

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
    email = forms.EmailField(label='email', max_length=50)

    def clean_username(self):
        # 对username的扩展验证，查找用户是否已经存在
        username = self.cleaned_data.get('username')
        users = models.UserInfo.objects.filter(username=username).count()
        if users:
            raise ValidationError('用户已经存在！')
        return username

    def clean_email(self):
        # 对email的扩展验证，查找用户是否已经存在
        email = self.cleaned_data.get('email')
        email_count = models.UserInfo.objects.filter(email=email).count() #从数据库中查找是否用户已经存在
        if email_count:
            raise ValidationError('该邮箱已经注册！')
        return email

    def _clean_new_password2(self): #查看两次密码是否一致
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError('两次密码不匹配！')

    def clean(self):
         #是基于form对象的验证，字段全部验证通过会调用clean函数进行验证
         self._clean_new_password2() #简单的调用而已

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = models.UserInfo.objects.filter(username=username).first()
        if username and password:
            if not user :
                raise ValidationError('用户不存在！')
            elif password != user.password:
                raise ValidationError('密码不正确！')
