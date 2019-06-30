from django.db import models

# Create your models here.
class Repo(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True)
    private = models.CharField(max_length=1, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)