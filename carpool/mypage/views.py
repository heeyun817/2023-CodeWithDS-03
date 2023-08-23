from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # User 모델 가져오기
from .models import UserProfile
from .forms import UserProfileForm

#전화번호, 프로필 사진만 변경 -> 이메일, 이름 변경 x
@login_required
def mypage(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    # User 모델에서 username, email, phone_number 가져오기
    user_profile.username = user.username
    user_profile.email = user.email
    user_profile.signup_date = user.date_joined
    user_profile.phone_number = user.userprofile.phone_number  # User 모델에서 phone_number 가져오기
    user_profile.save()

    return render(request, 'mypage.html', {'user_profile': user_profile})


@login_required
def edit_mypage(request):
    user = request.user  # 현재 로그인한 사용자
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        user.username = request.POST['username']
        user.save()
        if form.is_valid():
            form.save()
            return redirect('mypage:mypage')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_mypage.html',  {'form': form, 'user_profile': user_profile, 'request_user': request.user})




#기존 User모델만 사용 -> 사진 변경 안됨
# from django.shortcuts import render,redirect
# from accounts.models import User
# from django.contrib.auth.decorators import login_required
# from .forms import UserForm
#
# @login_required
# def mypage(request):
#     user = request.user
#     return render(request, 'mypage.html', {'user': user})
#
# #이미지만 수정 안됨
# @login_required
# def edit_mypage(request):
#     user = request.user  # 현재 로그인한 사용자
#     if request.method == 'POST':
#         # POST 요청을 처리하여 유저 데이터를 업데이트합니다.
#         user.username = request.POST['username']
#         user.email = request.POST['email']
#         # 이미지를 업로드한 경우에만 이미지 필드를 업데이트합니다.
#         if 'image' in request.FILES:
#             user.image = request.FILES["image"]
#
#         user.save()
#         return redirect('mypage:mypage')  # 수정 완료 후 마이페이지로 리디렉션
#
#     return render(request, 'edit_mypage.html', {'user': user})

































# @login_required
# def edit_mypage(request):
#     if request.method == 'POST' and request.FILES['image']:
#         image = request.FILES['image']
#         User.objects.create(image=image)
#         return redirect('mypage:mypage')  # 이미지 업로드 성공 후 이동할 뷰로 리디렉션
#     return render(request, 'mypage/edit_mypage.html')

# #수정 사항 반영 안됨
# @login_required
# def edit_mypage(request):
#     user = request.user
#
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('mypage:mypage')  # 수정 후 마이페이지로 리다이렉트
#     else:
#         form = UserProfileForm(instance=user)
#
#     return render(request, 'mypage/edit_mypage.html', {'form': form})
#












# #수정해야됨 - 편집 기능 안됨
# @login_required
# def edit_mypage(request):
#     user = request.user
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('mypage:mypage')  # Redirect to the mypage after successful update
#     else:
#         form = UserProfileForm(instance=user)
#
#     return render(request, 'mypage/edit_mypage.html', {'form': form})


# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from accounts.models import UserProfile
#
# #프로필 화면
# @login_required
# def mypage(request):
#     profile = UserProfile.objects.get(user=request.user)
#     return render(request, 'mypage/mypage.html', {'profile': profile})
#
# #프로필 수정 - 이미지, bio까지만..
# @login_required
# def edit_profile(request):
#     profile = UserProfile.objects.get(user=request.user)
#
#     if request.method == 'POST':
#         # POST 요청을 처리하여 프로필 업데이트
#         new_bio = request.POST.get('new_bio')
#         new_image = request.FILES.get('new_image')
#
#         if new_image:
#             profile.profile_picture = new_image
#
#         if new_bio is not None:
#             profile.bio = new_bio
#
#         profile.save()
#         return redirect('mypage:mypage')
#
#     return render(request, 'mypage/edit_mypage.html', {'profile': profile})
#
# #사용 기록 - 내가 모집한 글
# #사용 기록 - 댓글단 글(아니면 채팅창 글)
