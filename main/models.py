from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class UserYear(models.Model):
    student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    year = models.CharField(max_length=30,)

class UserData(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,)
    Name=models.CharField(max_length=30)
    ItselfIntro=models.TextField(max_length=120)
    AdventureIntro=models.TextField(max_length=120)
    SkillsIntro=models.TextField(max_length=120)
    JobIntro=models.TextField(max_length=120)
    SchollingIntro=models.TextField(max_length=360)
    ContactIntro=models.TextField(max_length=120)

