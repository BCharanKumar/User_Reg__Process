from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user_name=models.OneToOneField(User,on_delete=models.CASCADE)
    add=models.TextField()
    profil_pic=models.ImageField()


    def __str__(self):
        return str(self.user_name)