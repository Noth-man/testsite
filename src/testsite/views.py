from django.shortcuts import render
from django.views import generic
from .models import Threads, Comments
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'testsite/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thread_list'] = Threads.objects.all().order_by('-id')
        context['comment_list'] = Comments.objects.all()
        return context

class CreateThreadView(generic.TemplateView):
    template_name = 'testsite/createThread.html'

class ThreadView(generic.DetailView):
    model = Threads
    template_name = 'testsite/thread.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_list = Comments.objects.filter(thread_id=self.kwargs['pk'])
        context['comment_list'] = comment_list
        return context