from django.shortcuts import render, redirect
from django.views import generic
from .models import Threads, Comments
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'testsite/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thread_ids = Threads.objects.values_list('id').order_by('-id')[:10] # Threads Model 最新10件のid取得
        context['thread_list'] = Threads.objects.order_by('-id')[:10]
        context['comment_list'] = Comments.objects.filter(thread_id__in=thread_ids) 
        return context

class CreateThreadView(generic.TemplateView):
    template_name = 'testsite/createThread.html'

class ThreadView(generic.DetailView):
    model = Threads
    template_name = 'testsite/thread.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Comments.objects.filter(thread_id=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        message = self.request.POST.get("message")
        thread_id = self.request.POST.get("id")
        comment = Comments(thread_id=thread_id, body=message)
        comment.save()
        url = '/thread/' + thread_id + '/'
        return redirect(to=url)