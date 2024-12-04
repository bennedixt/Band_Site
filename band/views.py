from django.shortcuts import render
from .models import BandMember, Album, Concert
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from blog.models import Tour
from django.apps import apps
from .models import Tour


def home(request):
    """
    Renders the homepage with a list of albums, band members, and concerts.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        A rendered homepage template with context data.
    """
    albums = Album.objects.all()
    members = BandMember.objects.all()
    concerts = Concert.objects.all()
    context = {
        'albums': albums,
        'members': members,
        'concerts': concerts
    }
    return render(request, 'band/home.html', context)

def band_members(request):
    """
    Displays the list of all band members.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        A rendered template showing the band members.
    """
    members = BandMember.objects.all()
    return render(request, 'band/members.html', {'members': members})

def concerts(request):
    """
    Displays the list of all concerts.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        A rendered template showing the concerts.
    """
    concerts = Concert.objects.all()
    return render(request, 'band/concerts.html', {'concerts': concerts})

def signup(request):
    """
    Handles the user sign-up process.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        A rendered sign-up template with form data or redirects to login on successful submission.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def listen_now(request):
    """
    Displays the 'Listen Now' page for logged-in users.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        A rendered 'Listen Now' page for the logged-in user.
    """
    return render(request, 'band/listen_now.html')


def tour_dates(request):
    """
    Displays a list of upcoming tour dates for the band.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        A rendered template with a list of upcoming tours ordered by date.
    """
    tours = Tour.objects.all().order_by('date')
    return render(request, 'band_app/tours.html', {'tours': tours})


Tour = apps.get_model('band', 'Tour')

