from django.urls import path
from weather_api.views import WeatherAPIView

urlpatterns = [
    path('weather', WeatherAPIView.as_view(), name='weather'),
]
