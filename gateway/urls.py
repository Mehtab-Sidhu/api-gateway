from django.urls import path
from .views import APIGatewayView, get_weather, get_news

urlpatterns = [
    path('weather/', get_weather, name='get_weather'),
    path('news/', get_news, name="get_news")
]