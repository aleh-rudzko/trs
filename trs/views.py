from django.shortcuts import render


def index(request, path=''):
    """
    Renders the Angular2
    """
    return render(request, template_name='base.html')

