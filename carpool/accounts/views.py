from django.contrib import auth 
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from django.shortcuts import render, redirect

# 회원가입
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if request.POST['password1'] == request.POST['password2']:
                # 이메일 주소 검사: @duksung.ac.kr 도메인 확인
                email = form.cleaned_data['email'] 
                if not email.endswith('@duksung.ac.kr'):
                    return render(request, 'signup.html', {'error': '덕성여자대학교 이메일 주소를 사용해야 합니다.'})
                
                user = form.save()
            
                # 랜덤 숫자 생성
                random_number = str(random.randint(1000, 9999))

                # 이메일 보내기
                send_mail(
                    '이메일 인증 코드',
                    f'인증 코드: {random_number}',
                    'your_email@duksung.ac.kr',  # 보내는 이메일 계정
                    [user.email],
                    fail_silently=False,
                )
                
                # 랜덤 숫자를 verify_email 뷰로 전달하도록 수정
                return render(request, 'verify_email.html', {'random_number': random_number})
            else:
                return render(request, 'signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
        else:
            form = UserCreationForm()
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

# 이메일 인증 (랜덤 코드 보내서 인증하는 걸로 했습니다.)
def verify_email(request):
    if request.method == 'POST':
        user_entered_code = request.POST['verification_code']
        random_number = request.POST.get('random_number')  # 랜덤 숫자 가져오기
        if user_entered_code == random_number:  # 사용자가 입력한 코드와 랜덤 코드 비교
            # 인증 완료 후 로그인 처리
            user = User.objects.get(email=request.user.email)  # 이메일로 사용자 조회
            auth.login(request, user)
            return redirect('/')
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

# 헐@.. 계좌연결안함 ;;