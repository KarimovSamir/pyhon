from django.contrib import admin
from .models import GPSTracker

@admin.register(GPSTracker)
class GPSTrackerAdmin(admin.ModelAdmin):
    list_display = ('tracker_id', 'lat', 'lng', 'status')  # Поля, которые вы хотите отобразить в списке
    search_fields = ('tracker_id', 'status')  # Поля, по которым можно искать
    list_filter = ('status',)  # Фильтры справа
