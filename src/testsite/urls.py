from django.urls import path
from . import views

app_name = 'testsite'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('createThread/', views.CreateThreadView.as_view(), name='createThread'),
    path('thread/<int:pk>/', views.ThreadView.as_view(), name='thread'),
]