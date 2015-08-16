from django.shortcuts import render
from django.contrib.auth import views
# Create your views here.

def login(request, *args, **kwargs):
    if request.method == 'POST':
        if not request.data.get('remember_me', None):
            request.session.set_expiry(0)
    return views.login(request, *args, **kwargs)

