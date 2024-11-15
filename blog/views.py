
from django.shortcuts import render

def tour(request):
    return render(request, 'blog/tour.html')

def grammys(request):
    return render(request, 'blog/grammys.html')
