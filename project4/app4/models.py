from django.db import models
# Create your models here.
class mypage(models.Model): 
   myname = models.CharField(max_length = 50)
   myaddress = models.CharField(max_length = 50)

