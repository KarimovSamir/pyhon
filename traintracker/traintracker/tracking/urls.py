from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('track/', views.track, name='track'),
    path('map/<str:tracker_id>/', views.map_view, name='map_view'),
]
