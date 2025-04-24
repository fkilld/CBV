
from django.urls import path
"""
Module for configuring URL routing in the news application.
This module defines URL patterns that map specific endpoints to their corresponding 
class-based views, facilitating CRUD (Create, Read, Update, Delete) operations for news items.
- The root path ('') is routed to NewsListView, which displays a list of all news entries.
- The 'news/create/' endpoint is handled by NewsCreateView to enable the creation of new news entries.
- The 'news/<int:pk>/update/' endpoint maps to NewsUpdateView, allowing modification of an existing 
    news item identified by its primary key.
- The 'news/<int:pk>/delete/' route is assigned to NewsDeleteView, which handles the deletion of 
    a specified news item.
- The 'news/<int:pk>/' endpoint corresponds to NewsDetailView, providing detailed information on 
    a single news entry.
Each URL pattern plays a critical role in ensuring that the application supports comprehensive 
news management by delegating specific functionality to dedicated views.
"""

from .views import *

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]