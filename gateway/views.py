from django.shortcuts import render

import requests
from django.http import JsonResponse
from django.views import View
from django.core.cache import cache
from django.conf import settings
import os 

from .models import APILog

# Create your views here.

# Backend Service URLs 
SERVICES = {
    "weather": "http://127.0.0.1:8001/weather",
    "news": "https://newsapi.org/v2/top-headlines",
}

class APIGatewayView(View):
    def get(self, request, service_name):
        """
            Handles GET requests and forwards them to the appropriate backend service
        """
        if service_name not in SERVICES:
            return JsonResponse({"error": "Service not found"}, status=404)
        
        backend_url = SERVICES[service_name]

        # Check is response is in cache 
        cached_response = cache.get(backend_url)
        if cached_response:
            return JsonResponse(cached_response, safe=False)
        
        # Forward request to backend service 
        response = requests.get(backend_url, params=request.GET)

        # Log request
        log_entry = APILog.objects.create(
            method = "GET",
            endpoint = backend_url,
            request_data = dict(request.GET),
            response_data = response.json(),
            status_code = response.status_code,
        )

        # Cache the response for 120 seconds
        cache.set(backend_url, response.json(), timeout=120)

        return JsonResponse(response.json(), safe=False, status=response.status_code)

def get_weather(request):
    """
        Forward the request to Weather API
    """
    city = request.GET.get('city')

    if not city:
        return JsonResponse({"error": "city parameter is required"}, status=400)

    response = requests.get(f"{SERVICES['weather']}?city={city}")
    response.raise_for_status()

    log = APILog.objects.create(
        method = request.method,
        endpoint = request.path,
        request_data = {"city": city},
        response_data = response.json() if response.status_code==200 else {"error": "Failed to fetch weather"},
        status_code = response.status_code,
    )

    return JsonResponse(response.json(), status=response.status_code)

def get_news(request):
    """
        Fetch top headlines from News API
    """
    api_key = os.getenv("NEWSAPI_KEY")

    if not api_key:
        return JsonResponse({"error": "API Key missing"}, status=500)
    
    params = {
        "country": "us",
        "apiKey": api_key,
    }

    response = requests.get(SERVICES["news"], params=params)
    
    log = APILog.objects.create(
        method = request.method,
        endpoint = request.path,
        request_data = params,
        response_data = response.json() if response.status_code==200 else {"error": "Failed to fetch news"},
        status_code = response.status_code,
    )
    
    return JsonResponse(response.json(), status=response.status_code)