import requests
from django.shortcuts import render, get_object_or_404
from .models import GPSTracker

def home(request):
    return render(request, 'tracking/index.html')

def track(request):
    tracker_id = request.GET.get('tracker_id')
    tracker = get_object_or_404(GPSTracker, tracker_id=tracker_id)
    # location_name = get_location_name(tracker.lat, tracker.lng)
    location_name = 'Baku'
    return render(request, 'tracking/track.html', {'tracker': tracker, 'location_name': location_name})

def map_view(request, tracker_id):
    tracker = get_object_or_404(GPSTracker, tracker_id=tracker_id)
    # location_name = get_location_name(tracker.lat, tracker.lng)
    location_name = 'Baku'
    return render(request, 'tracking/map.html', {'tracker': tracker, 'location_name': location_name})

def get_location_name(lat, lng):
    try:
        response = requests.get(f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lng}&addressdetails=2")
        response.raise_for_status()  # Проверка на ошибки HTTP
        location_data = response.json()
        address = location_data.get('address', {})
        country = address.get('country', 'Неизвестная страна')
        city = address.get('city', address.get('state', ''))
        return f"{city}, {country}" if city else country
    except requests.RequestException as e:
        print(f"Ошибка при запросе к сервису геокодирования: {e}")
        return "Неизвестное местоположение"
