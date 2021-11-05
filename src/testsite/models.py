from django.db import models

# Create your models here.

class Threads(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class Meta:
       verbose_name_plural = "スレッド"

class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    thread_id = models.ForeignKey(Threads, on_delete=models.CASCADE)
    paremt_id = models.IntegerField()
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    class Meta:
       verbose_name_plural = "コメント"