from django.db import models

class BandMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='members/')  # Optional for pictures of band members

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='albums/')
    description = models.TextField()

    def __str__(self):
        return self.title

class Concert(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.location} on {self.date}"


class Band(models.Model):
    # The name of the band, displayed prominently on the site
    name = models.CharField(max_length=100)
    # Genre of music the band performs
    genre = models.CharField(max_length=50)
    # URL for the band's official website or social media
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.name  # Returns the name of the band when called

# band_app/models.py
from django.db import models

class Tour(models.Model):
    # Date and location of the tour
    date = models.DateField()
    location = models.CharField(max_length=100)
    # Optional field for ticket link
    ticket_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        # Returns a string with the tour date and location
        return f"{self.date} - {self.location}"
