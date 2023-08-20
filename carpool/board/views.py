from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import googlemaps
from carpool import settings


#def home(request):
    #return render(request, 'taxi_app/home.html', {'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY})

def calculate_taxi_fare(request):
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')

        # Google Maps API를 사용하여 출발지와 목적지 사이의 거리를 얻어와 택시비 계산
        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
        directions_result = gmaps.directions(origin, destination, mode="driving")
        if directions_result:
            distance_in_km = directions_result[0]['legs'][0]['distance']['value'] / 1000
            # 여기서 택시비 계산 로직을 구현하세요.

            return JsonResponse({'fare': calculated_fare})
        else:
            return JsonResponse({'error': 'Unable to calculate fare'})





def create(request):
    return render(request, 'create.html')


def taxi(request):
    return render(request, "copy.html")


def map(request):
    return render(request, "kakaomap.html")