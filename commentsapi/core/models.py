from django.db import models
from django.db.models.base import Model

class Comments(models.Model):
    email = models.EmailField(unique=True)
    comment = models.TextField(default="")
    
    comment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feed