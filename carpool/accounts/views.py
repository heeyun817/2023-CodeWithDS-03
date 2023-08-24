# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from .models import User
from .forms import CustomUserCreationForm
from django.contrib import auth

import random
from django.core.mail import send_mail

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

            
            if form.is_valid():
                # 랜덤 숫자 생성
                random_number = str(random.randint(1000, 9999))

                # 이메일 보내기
                send_mail(
                    'DukXi 이메일 인증 코드',
                    f'인증 코드: {random_number}',
                    'hmj6589@gmail.com',  # 보내는 이메일 계정
                    [email],
                    fail_silently=False,
                    )
                return render(request, 'verify_email.html', {'email': email, 'random_number': random_number})

            if password1 == password2:
                
                # random_number = str(random.randit(1000, 9999))

                # send_mail(
                #     'DukXi 이메일 인증 코드',
                #     f'인증 코드: {random_number}',
                #     'hmj6589@gmail.com',  # 보내는 이메일 계정
                #     [user.email],
                #     fail_silently=False,
                # )
                
                # if user_confirmation_code != random_number:
                #     error_message = '인증번호 오류'
                #     return render(request, 'verify_email.html', {'form': form, 'error': error_message})

                # 회원가입 정보 생성
                user = User.objects.create_user(username=username, password=password1)
                # user.save()
                user = form.save()

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

# # 이메일 인증
# def verify_email(request, confirmation_code):
#     if request.method == 'POST':
#         user_confirmation_code = request.POST.get('verification_code')
        
#         if user_confirmation_code == confirmation_code:
#             return redirect('accounts:signup')
        
#         else:
#             error_message = "인증번호가 일치하지 않습니다."
#             return render(request, 'verify_email.html', {'error': error_message})
#     else:
#         return render(request, 'verify_email.html', {'confirmation_code': confirmation_code})


# 이메일 인증 (랜덤 코드 보내서 인증하는 걸로 했습니다.)
def verify_email(request):
    if request.method == 'POST':
        user_entered_code = request.POST['verification_code']
        random_number = request.POST.get('random_number')
        if user_entered_code == random_number:
            # 인증 완료 후 회원가입 정보 생성 및 로그인 처리
            user = form.save()  # 회원가입 정보 생성
            auth_login(request, user)  # 로그인 처리
            return redirect('accounts:home')  # 로그인 이후 페이지로 이동
        else:
            return render(request, 'verify_email.html', {'error': '인증 코드가 일치하지 않습니다.'})
    else:
        return render(request, 'verify_email.html')

# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('accounts:home') # 그 다음 어딘가로..
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
