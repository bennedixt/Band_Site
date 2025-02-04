"""
Defines view functions for the Blog application.
"""

from django.shortcuts import render

def tour(request):
    """
    Renders the tour page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered tour template.
    """
    return render(request, 'blog/tour.html')

def grammys(request):
    """
    Renders the Grammys page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered Grammys template.
    """
    return render(request, 'blog/grammys.html')

