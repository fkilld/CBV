from django.contrib.auth.views import LogoutView
"""
Module: account/views.py
This module encapsulates the class-based views related to user account operations in a Django web application. 
Each view leverages Django's built-in generic views and authentication system to manage user interactions 
such as displaying the homepage, registering new users, logging in, and logging out.
Classes:
    HomeView:
        - Purpose: Renders the home page of the account application.
        - Details: Inherits from Django's TemplateView to serve static content. This page acts as a landing 
          page post-login or as a default informational view.
    RegisterView:
        - Purpose: Facilitates new user registration.
        - Details: Inherits from Django's CreateView and utilizes the built-in UserCreationForm to validate 
          and create new user entries. After successful registration, it redirects users to the login view, 
          ensuring a smooth transition into the authentication process.
    LoginView:
        - Purpose: Handles user login functionality.
        - Details: Extends Django's LoginView to display the login form. It specifies a custom template 
          for rendering the login page and sets a success URL to redirect authenticated users to the home page.
    LogoutView:
        - Purpose: Manages user logout processes.
        - Details: Inherits from Django's LogoutView without an associated template, simplifying the logout 
          process. By setting the next_page attribute, it ensures users are redirected to the home page after logging out.
Implementation Choices:
    - The use of Django's class-based generic views minimizes boilerplate code and improves maintainability.
    - The reverse_lazy function is employed for URL resolution, which defers evaluation until all URL configurations 
      have been loaded. This prevents potential circular import issues.
    - By leveraging built-in forms and views, the module ensures robust validation, security, and adherence to Django's 
      best practices for user authentication.
"""
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import *


class HomeView(TemplateView):
    """
    HomeView is a specialized view that renders the home page for the account section.
    It inherits from Django's TemplateView, enabling a straightforward mechanism to render
    a template without needing to write additional boilerplate code for handling HTTP methods.

    Key attributes:
        template_name (str): Specifies the path to the HTML template that will be rendered,
                             in this case 'account/home.html'.

    How It Works:
        - Upon receiving a GET request, HomeView leverages the built-in logic of TemplateView.
        - The get() method in the base class locates the specified template and renders it
          into an HTTP response.
        - Additional context can be provided by overriding the get_context_data() method if more
          dynamic content is needed in the template.

    Usage:
        - This view should be hooked into the URL configuration using HomeView.as_view(), which
          returns a callable view that can be used in URL patterns.
        - This design promotes clarity and simplicity for rendering a static template without
          extra logic unless explicitly customized.
    """
    template_name = 'account/home.html'


class RegisterView(CreateView):
    """
    Handles user registration by extending Django's generic CreateView.

    This view utilizes the built-in UserCreationForm to render and process the registration form.
    It specifies 'account/register.html' as the template for rendering the form and sets the
    success_url to the 'login' route using reverse_lazy, ensuring that users are redirected
    to the login page upon successful registration.

    Why this code is used:
    - Leverages Django's class-based views to efficiently manage form handling and object creation.
    - Uses UserCreationForm to simplify user registration by handling validation and saving of new users.
    - Ensures clean and maintainable code by reducing boilerplate typically required for form processing.
    - Utilizes reverse_lazy to defer URL resolution until it's needed, which is useful for avoiding 
        circular import issues in Django URL configurations.

    How it works:
    - On a GET request, the view renders the registration form using the specified template.
    - On a POST request, it processes the submitted form data. If the data is valid, a new user is created.
    - After successful form submission, users are automatically redirected to the login page using the
        defined success_url.
    """
    form_class = UserCreationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')
    
    
class LoginView(LoginView):
    """
    LoginView for handling user authentication.

    This class extends Django's built-in LoginView to customize the login process. It renders a 
    custom login template and redirects users to a specified URL upon successful authentication.

    Attributes:
        template_name (str): Path to the HTML template that renders the login page.
        success_url (ReverseLazy): URL to redirect users after a successful login, dynamically 
                                   resolved using Django's reverse_lazy, typically pointing to the 'home' route.

    How It Works:
        - When a user navigates to the login page, Django renders the template specified by template_name.
        - Upon submitting valid login credentials, the form is processed and, if authentication is successful,
          the user is redirected to the success_url.
        - This customization allows for a consistent user experience and seamless integration with the 
          overall site's navigation and routing structure.

    Why Use This Code:
        - To provide a tailored login interface that matches the application's design requirements.
        - To ensure proper redirection after login, maintaining a smooth user flow.
        - To leverage Django's robust authentication system while enabling easy customization of templates
          and post-login behavior.
    """
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')
    

# i want to make logout view without template
# views.py


class LogoutView(LogoutView):
    """
    A view that logs out the user and redirects to the home page.

    This LogoutView class extends Django's built-in LogoutView to handle user logout
    functionality. It overrides the default redirection after a logout by setting the
    next_page attribute to a lazily-evaluated URL resolved from the 'home' route. Using
    reverse_lazy ensures that URL resolution is deferred until it is needed at runtime,
    which prevents issues related to URL configurations that may not be loaded at the time
    of class definition.

    Overall, this class is used to facilitate a clean and efficient way to log a user out
    and redirect them to the designated home page.
    """
    next_page = reverse_lazy('home')








