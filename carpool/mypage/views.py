from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # User 모델 가져오기
from .forms import UserProfileForm
from .models import UserProfile
from board.models import Board
# from channels.models import ChatRoom
from accounts.models import User

#그냥 마이페이지
@login_required
def mypage(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    # User 모델에서 username, email, phone_number 가져오기
    user_profile.username = user.username
    user_profile.email = user.email
    user_profile.signup_date = user.date_joined
    # user_profile.phone_number = user.userprofile.phone_number  # User 모델에서 phone_number 가져오기
    user_profile.save()

    return render(request, 'mypage.html', {'user_profile': user_profile})

#이름, 프로필 사진만 변경 -> 이메일 변경 x
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


# 사용 기록 (자신이 작성 + 구함 완료까지) -> 다른 사용자 추가 하는 것도 구현 해야함
def completed_boards(request):
    user = request.user
    # 현재 사용자와 연결된 채팅방을 먼저 가져옵니다.
    # chat_rooms = ChatRoom.objects.filter(user_group=user)

    # 채팅방과 연결된 게시글을 가져옵니다.
    # completed_boards = Board.objects.filter(Q(completion=True, chatroom__in=chat_rooms) | Q(user=user, completion=True))
    completed_boards = Board.objects.filter(completion=True,member=user).distinct() #users=user
    return render(request, 'completed_boards.html', {'completed_boards': completed_boards})



# 다른 유저 프로필 보기
def view_profile(request, user_id):
    User = get_user_model()
    profile_user = get_object_or_404(User, pk=user_id)
    user_profile = get_object_or_404(UserProfile, user=profile_user)

    context = {
        'profile_user': profile_user,
        'user_profile': user_profile,
    }

    return render(request, 'profile_page.html', context)


#<!--게시글 작성자의 프로필로 이동하는 링크--> - board/detail.html에 추가하기
#<a href="{% url 'mypage:view_profile' board.user.id %}">{{ board.user.username }}</a>


# 자신이 작성한 글 보기(혹시 몰라서 한 번 넣어본 기능..)
def my_record(request):
    current_user = request.user
    my_posts = Board.objects.filter(user=current_user, completion=False)
    # comments = Comment.objects.filter(writer=current_user)

    return render(request, 'my_record.html', {
        'my_posts': my_posts,
        # 'comments': comments
    })
