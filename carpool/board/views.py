from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
#import googlemaps
from carpool import settings
from board.models import Board
# from board.models import WalkBoard
#from django.contrib.auth.models import User
from accounts.models import User
from channels.models import ChatRoom
import requests

#def home(request):
    #return render(request, 'taxi_app/home.html', {'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY})

# def calculate_taxi_fare(request):
#     if request.method == 'POST':
#         origin = request.POST.get('origin')
#         destination = request.POST.get('destination')

#         # Google Maps API를 사용하여 출발지와 목적지 사이의 거리를 얻어와 택시비 계산
#         gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
#         directions_result = gmaps.directions(origin, destination, mode="driving")
#         if directions_result:
#             distance_in_km = directions_result[0]['legs'][0]['distance']['value'] / 1000
#             # 여기서 택시비 계산 로직을 구현하세요.

#             return JsonResponse({'fare': calculated_fare})
#         else:
#             return JsonResponse({'error': 'Unable to calculate fare'})



def list(request):
    boardlist = Board.objects.all().order_by('-pk')
    return render(request, "list.html", {"boardlist": boardlist})


def create(request):
    print(request.user.pk)
    if request.method == "POST":   
        board = Board()
        board.user = User.objects.get(pk=request.user.pk)
        board.s_title = request.POST.get("start")
        board.d_title = request.POST.get("end")
        board.date = request.POST.get("date")
        board.people = int(request.POST.get("people")) #몇 명 모집?
        board.star = False
        board.content = request.POST.get("content")
        board.total = int(request.POST.get("total")) #금액
        board.completion = False
        board.now_people = 0
        board.save()
        board.member.add(request.user) #추가된 멤버
        chat_room = ChatRoom.objects.create(board=board)
        chat_room.user_group.add(request.user)
        return redirect("board:list")
    return render(request, 'kakaomap.html')


def detail(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, "detail.html", {"board":board})


def update(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        #board.user = board.user
        board.s_title = request.POST.get("start")
        board.d_title = request.POST.get("end")
        board.date = request.POST.get("date")
        board.people = request.POST.get("people")
        board.star = board.star
        board.content = request.POST.get("content")
        board.total = request.POST.get("total")
        completion_value = request.POST.get("completion")
        #다 구해지면 체크
        if completion_value == "on":
            board.completion = True
        elif completion_value == None:
            board.completion = False
        print("Completion value:", request.POST.get("completion"))

        board.now_people = request.POST.get("now_people")

        #현재 구한 사람과 구하려는 사람이 동일하다면 다 구해진 것
        if board.people == board.now_people and board.completion == False:
            board.completion = True
        board.save()
        return redirect("board:detail", pk)
    return render(request, "update.html", {"board": board})


def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    #목록으로 이동


def taxi(request):
    return render(request, "copy.html")


def map(request):
    return render(request, "kakaomap.html")


from django.http import JsonResponse

def proxy_request(request):
    url = request.GET.get('url')
    
    if not url:
        return JsonResponse({'error': 'URL parameter is missing'}, status=400)
    
    try:
        response = requests.get(url)
        return JsonResponse({'data': response.text})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

from .models import WalkBoard
from channels.models import WalkChatRoom
# 걷기

def walklist(request):
    boardlist = WalkBoard.objects.all().order_by('-pk')
    return render(request, "walklist.html", {"boardlist": boardlist})


def walkcreate(request):
    print(request.user.pk)
    if request.method == "POST":
        board = WalkBoard()
        board.user = User.objects.get(pk=request.user.pk)
        board.s_title = request.POST.get("start")
        board.d_title = request.POST.get("end")
        board.date = request.POST.get("date")
        board.people = int(request.POST.get("people")) #몇 명 모집?
        board.star = False
        board.content = request.POST.get("content")
        board.completion = False
        board.now_people = 0
        board.save()
        board.member.add(request.user) #추가된 멤버
        chat_room = WalkChatRoom.objects.create(board=board)
        chat_room.user_group.add(request.user)
        return redirect("board:walklist")
    return render(request, 'safemap.html')


def walkdetail(request, pk):
    board = WalkBoard.objects.get(pk=pk)
    return render(request, "walkdetail.html", {"board":board})


def walkupdate(request, pk):
    board = WalkBoard.objects.get(pk=pk)
    if request.method == "POST":
        #board.user = board.user
        board.s_title = request.POST.get("start")
        board.d_title = request.POST.get("end")
        board.date = request.POST.get("date")
        board.people = request.POST.get("people")
        board.star = board.star
        board.content = request.POST.get("content")
        board.total = request.POST.get("total")
        completion_value = request.POST.get("completion")
        #다 구해지면 체크
        if completion_value == "on":
            board.completion = True
        elif completion_value == None:
            board.completion = False
        print("Completion value:", request.POST.get("completion"))

        board.now_people = request.POST.get("now_people")

        #현재 구한 사람과 구하려는 사람이 동일하다면 다 구해진 것
        if board.people == board.now_people and board.completion == False:
            board.completion = True
        board.save()
        return redirect("board:walkdetail", pk)
    return render(request, "walkupdate.html", {"board": board})


def walkdelete(request, pk):
    try:
        board = WalkBoard.objects.get(pk=pk)
        board.delete()
        return redirect("board:walklist")  # 삭제 후에 어디로 리디렉션할지 설정하세요.
    except WalkBoard.DoesNotExist:
        # 해당 객체가 없을 경우 예외 처리
        return HttpResponse("Object not found", status=404)
    #목록으로 이동

def walkroad(request):
    return render(request, "walkroad.html")

def map_view(request):
    return render(request, 'safemap.html')

def walktaxi(request):
    return render(request, "walkcopy.html")

def boardmain(request):
    return render(request, "board.html")