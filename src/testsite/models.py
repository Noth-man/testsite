from django.db import models

# Create your models here.

class Threads(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    first_body = models.TextField(max_length=2500, blank=True, null=True)
    class Meta:
       verbose_name_plural = "スレッド"

class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    thread_id = models.IntegerField(blank=True, null=True)
    paremt_id = models.IntegerField(blank=True, null=True)
    body = models.TextField(max_length=2500)
    pub_date = models.DateTimeField(auto_now_add=True)
    class Meta:
       verbose_name_plural = "コメント"