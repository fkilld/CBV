from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import News

from django.urls import reverse_lazy



class NewsListView(LoginRequiredMixin, ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news_list"

    def get_queryset(self):
        return News.objects.all().order_by('-published_date')


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    fields = ["title", "content"]  # update fields as needed
    template_name = "news/news_form.html"
    success_url = reverse_lazy("news_list")  # update URL name as needed

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    fields = ["title", "content"]  # update fields as needed
    template_name = "news/news_form.html"
    success_url = reverse_lazy("news_list")  # update URL name as needed

    def get_queryset(self):
        # only allow the author to edit their own news
        return super().get_queryset().filter(author=self.request.user)


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    success_url = '/news/'

    def get(self, request, *args, **kwargs):
        # Bypass confirmation template and delete immediately
        return self.post(request, *args, **kwargs)

class NewsDetailView(LoginRequiredMixin, DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news"  # update context object name as needed
