from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.core.mail import send_mail
import random
from .forms import CustomUserCreationForm

# 회원가입
def signup(request):
    if request.method == 'POST':
        step = request.POST.get('step', 1)  # 현재 단계를 받아옵니다.

        if step == '1':  # 이메일 작성 단계
            form = CustomUserCreationForm(request.POST)
            email = form['email'].value()
            
            if not email.endswith('@duksung.ac.kr'):
                error_message = '덕성여자대학교 이메일 주소를 사용해야 합니다.'
                return render(request, 'signup.html', {'form': form, 'step': '1', 'error': error_message})

            if form.is_valid():
                # 랜덤 숫자 생성
                random_number = str(random.randint(1000, 9999))

                # 이메일 보내기
                send_mail(
                    '이메일 인증 코드',
                    f'인증 코드: {random_number}',
                    'hmj6589@gmail.com',  # 보내는 이메일 계정
                    [email],
                    fail_silently=False,
                )

                return render(request, 'verify_email.html', {'random_number': random_number, 'email': email, 'step': '2'})

        elif step == '2':  # 이메일 인증 단계
            user_entered_code = request.POST['verification_code']
            random_number = request.POST.get('random_number')
            if user_entered_code == random_number:
                return render(request, 'signup.html', {'email': request.POST['email'], 'step': '3'})
            else:
                return render(request, 'verify_email.html', {'error': '인증 코드가 일치하지 않습니다.'})

        elif step == '3':  # 비밀번호 작성 단계
            email = request.POST['email']
            return render(request, 'signup.html', {'email': email, 'step': '4'})

        elif step == '4':  # 비밀번호 확인 단계
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                # 이메일 주소 검사: @duksung.ac.kr 도메인 확인
                if not email.endswith('@duksung.ac.kr'):
                    return render(request, 'signup.html', {'error': '덕성여자대학교 이메일 주소를 사용해야 합니다.'})

                user = CustomUserCreationForm(request.POST).save()  # 회원가입 정보 생성
                auth_login(request, user)  # 로그인 처리
                return redirect('home')  # 로그인 이후 페이지로 이동
            else:
                return render(request, 'signup.html', {'email': email, 'step': '3', 'error': '비밀번호가 일치하지 않습니다.'})

    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form, 'step': '1'})


# 이메일 인증 (랜덤 코드 보내서 인증하는 걸로 했습니다.)
def verify_email(request):
    if request.method == 'POST':
        user_entered_code = request.POST['verification_code']
        random_number = request.POST.get('random_number')
        if user_entered_code == random_number:
            # 인증 완료 후 회원가입 정보 생성 및 로그인 처리
            user = form.save()  # 회원가입 정보 생성
            auth_login(request, user)  # 로그인 처리
            return redirect('home')  # 로그인 이후 페이지로 이동
        else:
            return render(request, 'verify_email.html', {'error': '인증 코드가 일치하지 않습니다.'})
    else:
        return render(request, 'verify_email.html')

# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
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
