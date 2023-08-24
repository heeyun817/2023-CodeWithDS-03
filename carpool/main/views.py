from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from board.models import Board



#검색 기능
def search(request):
    return render(request, 'search.html')

def search_result(request):
    search_text = request.GET.get('search_text', '')
    search_type = request.GET.get('search_type', '')

    if search_text and search_type:
        # "수유역" 버튼을 누른 경우 출발지 필드 또는 도착지 필드와 일치하는 결과를 반환
        if search_text == '수유역':
            if search_type == 's_title': #출발지 검색 -> 덕대로 도착
                search_results = Board.objects.filter(Q(s_title__icontains=search_text)&(Q(d_title__icontains='덕성여자대학교')|Q(d_title__icontains='덕성여대')))
            elif search_type == 'd_title': #덕대에서 출발 -> 도착지 검색
                search_results = Board.objects.filter(Q(d_title__icontains=search_text)&(Q(s_title__icontains='덕성여자대학교')|Q(s_title__icontains='덕성여대')))
        elif search_text == '서울역':
            if search_type == 's_title':
                search_results = Board.objects.filter(Q(s_title__icontains=search_text)&(Q(d_title__icontains='덕성여자대학교')|Q(d_title__icontains='덕성여대')))
            elif search_type == 'd_title':
                search_results = Board.objects.filter(Q(d_title__icontains=search_text)&(Q(s_title__icontains='덕성여자대학교')|Q(s_title__icontains='덕성여대')))
        elif search_text == '덕성여대 정문':
            if search_type == 's_title':
                search_results = Board.objects.filter((Q(s_title__icontains=search_text)|Q(s_title__icontains='덕성여자대학교 정문'))&(Q(d_title__icontains='덕성여자대학교')|Q(d_title__icontains='덕성여대')))#(Q(s_title__icontains=search_text)|Q(s_title__icontains='덕성여자대학교 정문'))
            elif search_type == 'd_title':
                search_results = Board.objects.filter((Q(d_title__icontains=search_text)|Q(d_title__icontains='덕성여자대학교 정문'))&(Q(s_title__icontains='덕성여자대학교')|Q(s_title__icontains='덕성여대')))
        elif search_text == '덕성여대 후문':
            if search_type == 's_title':
                search_results = Board.objects.filter((Q(s_title__icontains=search_text)|Q(s_title__icontains='덕성여자대학교 후문'))&(Q(d_title__icontains='덕성여자대학교')|Q(d_title__icontains='덕성여대')))
            elif search_type == 'd_title':
                search_results = Board.objects.filter((Q(d_title__icontains=search_text)|Q(d_title__icontains='덕성여자대학교 후문'))&(Q(s_title__icontains='덕성여자대학교')|Q(s_title__icontains='덕성여대')))
        else:
            # 일반 검색 쿼리 처리
            if search_type == 's_title':
                search_results = Board.objects.filter(Q(s_title__icontains=search_text)&(Q(d_title__icontains='덕성여자대학교')|Q(d_title__icontains='덕성여대')))
            elif search_type == 'd_title':
                search_results = Board.objects.filter(Q(d_title__icontains=search_text)&(Q(s_title__icontains='덕성여자대학교')|Q(s_title__icontains='덕성여대')))
    else:
        search_results = []

    return render(request, 'search_result.html', {'search_results': search_results})



# #즐겨 찾기 게시물 페이지
# @login_required
# def starred_boards(request):
#     # 이제 이 뷰 함수는 로그인된 사용자만 접근 가능합니다.
#     user = request.user
#     starred_boards = StarredBoard.objects.filter(user=user).select_related('board')
#     return render(request, 'starred_boards.html', {'starred_boards': starred_boards})
#
#
# #즐겨 찾기 토글 기능
# def toggle_star(request, board_id):
#     board = get_object_or_404(Board, pk=board_id)
#     user = request.user
#     try:
#         # 이미 즐겨찾기한 경우, 즐겨찾기 취소
#         starred_board = StarredBoard.objects.get(user=user, board=board)
#         starred_board.delete()
#     except StarredBoard.DoesNotExist:
#         # 즐겨찾기하지 않은 경우, 즐겨찾기 추가
#         StarredBoard.objects.create(user=user, board=board)
#     return redirect('board_detail', board_id=board_id)
#
