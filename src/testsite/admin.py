from django.contrib import admin
from .models import Threads, Comments
# Register your models here.

class ThreadsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'thread_id', 'paremt_id', 'body', 'pub_date')

admin.site.register(Threads, ThreadsAdmin)
admin.site.register(Comments, CommentsAdmin)