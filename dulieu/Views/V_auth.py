from django import forms
import re
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ..FORMS.form_resign import ResignForm
# Create your views here.
def LoginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        error=None
        succes=None
        print(username,password)
        if user is not None:
            login(request, user)
            succes='dang nhập thành công'
        else:
            error='Tên đăng nhập hoặc mật khẩu không chính xác'
        content = {'error': error, 'succes': succes}
        return render(request, 'Auth/login.htm',content)
    else:
        return render(request,'Auth/login.htm')
from django.contrib.auth import logout
def LogOutPage(request):
    logout(request)
    return redirect('loginpage')


def ResignPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        error=None
        succes=None
        user=None
        if not username:
            error='Vui lòng điền tên đăng nhập'
        elif not re.search(r'^[a-zA-Z0-9]*$',username):
            error='tài khoản chứa ký tự không hộp lệ'
        elif not re.search(r'^[a-zA-Z0-9]*$', password1):
            error='Mật khẩu chứa ký tự không hợp lệ'
        elif not re.search(r"[\d]+", password1):
            error='Mật khẩu phải chứa ít nhất 1 số'
        elif len(password1)<=7:
            error='Mật khảu phải có ít nhất 8 ký tự'
        elif password1 != password2:
            error='Mật khảu nhập lại không đúng'

        else:
            try:
                User.objects.get(username=username)
                error='tài khoản đã tồn tại'
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                succes = 'Tài khoản đăng ký thành công'



        print(username)
        content={'error':error,'succes':succes}
        return render(request,'Auth/resign.htm',content)
    else:


        form=ResignForm()
        content={'form':form,}
        return render(request,'Auth/resign.htm',content)