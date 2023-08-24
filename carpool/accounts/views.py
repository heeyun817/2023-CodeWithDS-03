# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from .models import User
from .forms import CustomUserCreationForm
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print("여기")
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
                
            # 이메일 주소 검사: @duksung.ac.kr 도메인 확인
            if not email.endswith('@duksung.ac.kr'):
                error_message = '덕성여자대학교 이메일 주소를 사용해야 합니다.'
                return render(request, 'signup.html', {'form': form, 'error': error_message})

            if password1 == password2:
                    # 회원가입 정보 생성
                user = User.objects.create_user(username=username, password=password1)
                user.save()

                return redirect('accounts:home')  # 로그인 이후 페이지로 이동
            else:
                error_message = '비밀번호가 일치하지 않습니다.'
                return render(request, 'signup.html', {'form': form, 'error': error_message})
        else:
                # 폼이 유효하지 않은 경우 오류 메시지와 함께 폼을 다시 렌더링
            return render(request, 'signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})




# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('') # 그 다음 어딘가로..
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('') # 그 다음 어딘가로...

# 회원가입, 로그인, 로그아웃 모여있는 
def home(request):
    return render(request, 'home.html')
