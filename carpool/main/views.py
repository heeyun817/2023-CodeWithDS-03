from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from board.models import Board, WalkBoard



#검색 기능
def search(request):
    return render(request, 'search.html')

def search_result(request):
    search_text = request.GET.get('search_text', '')
    search_type = request.GET.get('search_type', '')
    transport_type = request.GET.get('transport_type', '')
    if transport_type == 'taxi': #택시
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
            elif search_text == '덕성여대':
                if search_type == 's_title':
                    search_results = Board.objects.filter((Q(s_title__icontains=search_text)|Q(s_title__icontains='덕성여자대학교'))&(Q(d_title__icontains='덕성여자대학교')|Q(d_title__icontains='덕성여대')))#(Q(s_title__icontains=search_text)|Q(s_title__icontains='덕성여자대학교 정문'))
                elif search_type == 'd_title':
                    search_results = Board.objects.filter((Q(d_title__icontains=search_text)|Q(d_title__icontains='덕성여자대학교'))&(Q(s_title__icontains='덕성여자대학교')|Q(s_title__icontains='덕성여대')))
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
    elif transport_type == 'walk': # 걷기
        if search_text and search_type:
            # "수유역" 버튼을 누른 경우 출발지 필드 또는 도착지 필드와 일치하는 결과를 반환
            if search_text == '수유역':
                if search_type == 's_title':  # 출발지 검색 -> 덕대로 도착
                    search_results = WalkBoard.objects.filter(Q(s_title__icontains=search_text) & (
                                Q(d_title__icontains='덕성여자대학교') | Q(d_title__icontains='덕성여대')))
                elif search_type == 'd_title':  # 덕대에서 출발 -> 도착지 검색
                    search_results = WalkBoard.objects.filter(Q(d_title__icontains=search_text) & (
                                Q(s_title__icontains='덕성여자대학교') | Q(s_title__icontains='덕성여대')))
            elif search_text == '서울역':
                if search_type == 's_title':
                    search_results = WalkBoard.objects.filter(Q(s_title__icontains=search_text) & (
                                Q(d_title__icontains='덕성여자대학교') | Q(d_title__icontains='덕성여대')))
                elif search_type == 'd_title':
                    search_results = WalkBoard.objects.filter(Q(d_title__icontains=search_text) & (
                                Q(s_title__icontains='덕성여자대학교') | Q(s_title__icontains='덕성여대')))
            elif search_text == '덕성여대':
                if search_type == 's_title':
                    search_results = WalkBoard.objects.filter(
                        (Q(s_title__icontains=search_text) | Q(s_title__icontains='덕성여자대학교')) & (
                                    Q(d_title__icontains='덕성여자대학교') | Q(
                                d_title__icontains='덕성여대')))  # (Q(s_title__icontains=search_text)|Q(s_title__icontains='덕성여자대학교 정문'))
                elif search_type == 'd_title':
                    search_results = WalkBoard.objects.filter(
                        (Q(d_title__icontains=search_text) | Q(d_title__icontains='덕성여자대학교')) & (
                                    Q(s_title__icontains='덕성여자대학교') | Q(s_title__icontains='덕성여대')))
            elif search_text == '덕성여대 후문':
                if search_type == 's_title':
                    search_results = WalkBoard.objects.filter(
                        (Q(s_title__icontains=search_text) | Q(s_title__icontains='덕성여자대학교 후문')) & (
                                    Q(d_title__icontains='덕성여자대학교') | Q(d_title__icontains='덕성여대')))
                elif search_type == 'd_title':
                    search_results = WalkBoard.objects.filter(
                        (Q(d_title__icontains=search_text) | Q(d_title__icontains='덕성여자대학교 후문')) & (
                                    Q(s_title__icontains='덕성여자대학교') | Q(s_title__icontains='덕성여대')))
            else:
                # 일반 검색 쿼리 처리
                if search_type == 's_title':
                    search_results = WalkBoard.objects.filter(Q(s_title__icontains=search_text) & (
                                Q(d_title__icontains='덕성여자대학교') | Q(d_title__icontains='덕성여대')))
                elif search_type == 'd_title':
                    search_results = WalkBoard.objects.filter(Q(d_title__icontains=search_text) & (
                                Q(s_title__icontains='덕성여자대학교') | Q(s_title__icontains='덕성여대')))
        else:
            search_results = []

        return render(request, 'walksearch_result.html', {'search_results': search_results})
