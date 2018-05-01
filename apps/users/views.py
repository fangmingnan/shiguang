from django.shortcuts import render,HttpResponseRedirect
from django.views import View
from users.form import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from users.models import UserInfo

# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserInfo.objects.get(Q(username=username) | Q(email=username))   #查询username等于数据库中用户名或者邮箱的
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# 首页
class Index_view(View):
    def get(self,request):
        return render(request,'index.htm',{})


# 登录页面
class LoginView(View):
    def get(self,request):
        return render(request,'login.html',{})

    def post(self,request):
        login_form = LoginForm(request.POST)        # 获取登录的数据
        if login_form.is_valid():                   # 验证是否有效
            user_name = request.POST.get('username','')
            pass_word = request.POST.get('password','')
            user = authenticate(username = user_name,password = pass_word)   #验证user
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reversed('index'))
            else:
                return render(request,'login.html',{'msg':'账号密码有误'})
        return render(request,'login.html',{'login_form':login_form})    #账号无效，错误信息回填


# 注销
class LogoutView(View):
    def get(self,request):
        logout(request)
        return render(request,'index.htm',{})