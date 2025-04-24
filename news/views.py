from django.shortcuts import render
"""
Detailed documentation for the news/views.py module.
This module defines several Django class-based views for managing News objects.
Each view is secured with LoginRequiredMixin to ensure that only authenticated users
can access the news functionalities. The views leverage Django's generic views to
simplify common operations like listing, creating, updating, deleting, and viewing
detailed content of news items.
Classes:
----------

Overall Design Considerations:
--------------------------------
- Security: By extending LoginRequiredMixin, all views enforce that only
  authenticated users may interact with the news module, thereby maintaining
  the privacy and integrity of the application.
- Maintainability: Utilizing Django’s generic class-based views avoids redundant
  code and adheres to the DRY (Don't Repeat Yourself) principle.
- Flexibility: Each view is designed to be extendable and easy to modify, making
  it straightforward to adapt to additional requirements or changes in the data model.
- URL Handling: The use of reverse_lazy ensures that URL resolution is deferred
  until necessary, accommodating dynamic application configuration and avoiding
  circular import issues.
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import News

from django.urls import reverse_lazy


"""
NewsListView:
    - Inherits from LoginRequiredMixin and ListView.
    - Purpose:
        * Display a list of news articles.
        * The get_queryset method is overridden to return news sorted by the
          published_date in descending order, ensuring the most recent news
          is shown first.
    - Rationale:
        * Utilizing ListView abstracts much of the list handling logic,
          including pagination and context management.
        * Ensuring only logged-in users can view the news list maintains data privacy.
        """


class NewsListView(LoginRequiredMixin, ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news_list"

    def get_queryset(self):
        return News.objects.all().order_by('-published_date')

"""

NewsCreateView:
    - Inherits from LoginRequiredMixin and CreateView.
    - Purpose:
        * Provide an interface to create new news articles.
        * Uses a form that includes title and content fields.
    - Key Implementation Details:
        * Overrides form_valid to automatically set the author field as the
          current logged-in user.
        * Uses reverse_lazy to redirect to the news list after successful creation.
    - Rationale:
        * This pattern enforces that each created news article is associated
          with its creator, enhancing data integrity and accountability.
        * The use of CreateView simplifies form handling and validation.
        
    """
class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    fields = ["title", "content"]  # update fields as needed
    template_name = "news/news_form.html"
    success_url = reverse_lazy("news_list")  # update URL name as needed

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


"""
NewsUpdateView:
    - Inherits from LoginRequiredMixin and UpdateView.
    - Purpose:
        * Allow authors to update their own news articles.
        * The get_queryset method is overridden to restrict the update
          operations to only those news items created by the logged-in user.
    - Rationale:
        * This approach ensures that users cannot modify news articles that
          they do not own, thereby reinforcing security and data consistency.
        * It leverages Django's built-in update functionalities to reduce code redundancy.
          """
class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    fields = ["title", "content"]  # update fields as needed
    template_name = "news/news_form.html"
    success_url = reverse_lazy("news_list")  # update URL name as needed

    def get_queryset(self):
        # only allow the author to edit their own news
        return super().get_queryset().filter(author=self.request.user)


"""

NewsDeleteView:
    - Inherits from LoginRequiredMixin and DeleteView.
    - Purpose:
        * Delete news articles.
        * Overrides the get method to bypass the traditional confirmation
          template and immediately proceed with deletion.
        * Redirects to a defined success_url after deletion.
    - Rationale:
        * Immediate deletion can streamline user interaction where a confirmation
          step is unnecessary or handled elsewhere.
        * Using DeleteView efficiently encapsulates the deletion logic while
          preserving consistency with other CRUD operations.

          
          """
class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    success_url = '/news/'

    def get(self, request, *args, **kwargs):
        # Bypass confirmation template and delete immediately
        return self.post(request, *args, **kwargs)

"""
NewsDetailView:
    - Inherits from LoginRequiredMixin and DetailView.
    - Purpose:
        * Display detailed information about a single news article.
        * Sets a custom context object name for use within the template.
    - Rationale:
        * Offers a clear and focused presentation of news article details.
        * Ensures only authenticated users can access sensitive content,
          protecting user and news data.
          
        """
class NewsDetailView(LoginRequiredMixin, DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news"  # update context object name as needed
