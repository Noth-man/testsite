from django.db import models

# Create your models here.

class Threads(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=100)

class Comments(models.Model):
    id = models.IntegerField()
    thread_id = models.ForeignKey(Threads, on_delete=models.CASCADE)
    paremt_id = models.IntegerField()
    body = models.TextField()
    pub_date = models.DateTimeField('date published')