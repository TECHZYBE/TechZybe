from django.db import models
from datetime import datetime  
from datetime import datetime  
from django.utils.timezone import now
# Create your models here.
class Contact_details(models.Model):
    name = models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    message=models.CharField(max_length=100)
    time=models.DateTimeField(default=now, blank=True)
