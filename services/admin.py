from django.contrib import admin
from .models import Service,ServiceRequest

# Register your models here.
admin.site.register(ServiceRequest)
admin.site.register(Service)