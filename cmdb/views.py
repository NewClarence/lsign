# -*- coding: UTF-8 -*-

from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponse
from django.contrib import messages
from cmdb import models,forms

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):

    if request.method == "POST":
	form = forms.RegisterForm(request.POST)
	if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
	    email = form.cleaned_data['email']
            models.UserInfo.objects.create(username=username, password=password,email=email)
	    return render(request,'cmdb/register_ok.html')
    else:
	form = forms.RegisterForm()
    return render(request, "cmdb/register.html", {"form": form})

def login(request):

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
	if form.is_valid():
	    username = form.cleaned_data['username']
	    password = form.cleaned_data['password']
	    user = models.UserInfo.objects.filter(username__exact=username, password__exact=password)
	    if user:
		return render_to_response('cmdb/success.html', {'username': username})
    else:
	form = forms.LoginForm()

    return render(request,'cmdb/login.html',{'form':form})
