from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Threads, Comments
# Create your views here.

class IndexView(TemplateView):
    template_name = 'testsite/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thread_list'] = Threads.objects.all()
        context['comment_list'] = Comments.objects.all()
        return context

class CreateThreadView(TemplateView):
    template_name = 'testsite/createThread.html'
