from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Fling(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255) #textfield will give a big text field box but charfield will give a single line blank box
    photo = models.ImageField(upload_to="photos/",blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) #difference between auto_now_add and auto_now is that the created_at field is added at the current
    #time when the object is created and the auto_now field is updated every time the object is updated in the same entry

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}' 
