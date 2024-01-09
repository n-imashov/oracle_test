from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
import requests
from datetime import datetime, timedelta
from django.core.cache import cache


class WeatherAPIView(APIView):
    API_KEY = '7ad461fb9956c78c0e4fceacf5dcd792'

    def get_weather_data(self, city_name):
        cache_key = f'weather_cache_{city_name}'
        cached_data = cache.get(cache_key)
        if cached_data and (datetime.now() - cached_data['timestamp']).seconds < 1800:
            return cached_data['data']

        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.API_KEY}&units=metric'
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = {
                'temperature': response.json()['main']['temp'],
                'pressure': response.json()['main']['pressure'],
                'wind_speed': response.json()['wind']['speed'],
            }

            cache.set(cache_key, {'data': weather_data, 'timestamp': datetime.now()})
            return weather_data
        else:
            return None

    def get(self, request):
        city_name = request.query_params.get('city', '')
        if not city_name:
            return JsonResponse({'error': 'City name is required'}, status=status.HTTP_400_BAD_REQUEST)

        weather_data = self.get_weather_data(city_name)

        if weather_data:
            return JsonResponse(weather_data)
        else:
            return JsonResponse({'error': 'Failed to retrieve weather data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
