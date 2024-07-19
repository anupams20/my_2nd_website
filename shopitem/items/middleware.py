from django.shortcuts import redirect
from django.urls import reverse

class Restrictaccess:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define URLs that are accessible without authentication
        allowed_urls = [
            reverse('login'),
            reverse('signup'),
            #reverse('password_change'),
        ]
        
        # If the user is not authenticated and the request URL is not in the allowed URLs, redirect to login
        if not request.user.is_authenticated and request.path not in allowed_urls:
            return redirect('login')
        
        response = self.get_response(request)
        return response
