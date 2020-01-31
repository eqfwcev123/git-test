from django.db import models


# Create your models here.

class PostModel(models.Model):
    created_date = models.DateTimeField(auto_created=True)
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
