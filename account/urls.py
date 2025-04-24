
from django.urls import path
"""
URL Configuration for the account app.
This module defines the URL patterns for the account-related views in the application.
Each URL pattern is associated with a specific view and a name for easy reference.
Routes:
- 'register/': Maps to the `RegisterView` class-based view. Used for user registration.
- 'login/': Maps to the `LoginView` class-based view. Used for user authentication.
- 'logout/': Maps to the `LogoutView` class-based view. Used for logging out users.
- 'home/': Maps to the `HomeView` class-based view. Displays the home page for authenticated users.
Attributes:
- urlpatterns (list): A list of `path` objects that define the URL patterns for the app.
"""
from .views import RegisterView, LoginView, LogoutView, HomeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
]
