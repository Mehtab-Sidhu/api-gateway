from django.contrib import admin
from .models import APILog

# Register your models here.
@admin.register(APILog)
class APIAdmin(admin.ModelAdmin):
    list_display = ('id', 'method', 'endpoint', 'request_data', 'response_data', 'status_code', 'created_at')