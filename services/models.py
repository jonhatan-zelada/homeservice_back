from django.db import models
from datetime import datetime
# Create your models here.

class Service(models.Model):
    service_code = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100)
    responsible = models.CharField(max_length=50)

    def __str__ (self) :
        return self.service_name

class ServiceRequest(models.Model):
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    reporter=models.CharField(max_length=60)
    detail_request=models.TextField(max_length=250,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__ (self) :
        return '%s %s' % (self.service, self.reporter)