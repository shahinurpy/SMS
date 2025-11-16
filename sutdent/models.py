from django.db import models
from django.conf import settings
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True,related_name='admin_profile')
    
    name = models.CharField(max_length=200, blank=True,  null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile", blank=True, null=True)
    joined_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.user.email if self.user else "No User"