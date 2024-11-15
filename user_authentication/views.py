# user_authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # redirect to the homepage or any restricted content
    else:
        form = UserCreationForm()
    return render(request, 'user_authentication/register.html', {'form': form})
