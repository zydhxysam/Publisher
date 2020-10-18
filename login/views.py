from django.shortcuts import render,HttpResponse,redirect
from login import models


def index(request):

    return render(request,'index.html')

def login(request):
    #从页面获取用户输入用户名和密码，访问方式POST
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('password')

        if models.User.objects.filter(username=user,password=pwd):
            return redirect('/index/')
        return render (request,'login.html',{'error':'用户名或密码错误'})
    return render(request,'login.html')

