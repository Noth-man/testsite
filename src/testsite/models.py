from django.db import models

# Create your models here.

class Threads(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
       verbose_name_plural = "スレッド"

class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    thread_id = models.IntegerField(blank=True, null=True)
    paremt_id = models.IntegerField(blank=True, null=True)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    class Meta:
       verbose_name_plural = "コメント"