from pyexpat import model
from statistics import mode
from django.db import models
import datetime
# Create your models here.

class videoUpload(models.Model):
    video=models.FileField(upload_to='media',null=True)
    date_uploaded = models.DateTimeField(blank=True, null=True,default=datetime.date.today)