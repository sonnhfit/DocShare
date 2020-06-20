from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django import views 
from django.contrib.auth import get_user_model, authenticate, login
User = get_user_model()
# Create your views here.


class SignUpView(views.View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        user_name = request.POST['user_name']
        email = request.POST['email']
        pass_word1 = request.POST['pass_word1']
        pass_word2 = request.POST['pass_word2']

        if pass_word1==pass_word2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'tên người dùng đã tồn tại')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email đã tồn tại')
            else:
                user = User.objects.create_user(username=user_name, password=pass_word1, email=email)
                user.save();
        else:
            messages.info(request, 'mật khẩu không khớp')
        return redirect('sign_up')


class SignInView(views.View):
    def get(self, request):
        return render(request, 'login.html', )

    def post(self, request):
        user_name = request.POST.get('user_name')
        pass_word = request.POST.get('pass_word')
        check = authenticate(username=user_name, password=pass_word)
    
        if check is None:
            messages.info(request, 'mật khẩu hoặc email của bạn nhập không đúng')
            return redirect('sign_in')
        login(request, check)
        return redirect('home')

    