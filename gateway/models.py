from django.db import models

# Create your models here.
class APILog(models.Model):
    method = models.CharField(max_length=10)    # HTTP method
    endpoint = models.CharField(max_length=255)     # Requested API endpoint
    request_data = models.JSONField(null=True, blank=True)      # Request payload
    response_data = models.JSONField(null=True, blank=True)     # API Response 
    status_code = models.IntegerField()     # HTTP status code
    created_at = models.DateTimeField(auto_now_add=True)    # Timestamp

    def __str__(self):
        return f"{self.method} {self.endpoint} - {self.status_code}"