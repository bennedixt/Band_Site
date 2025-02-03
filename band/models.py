from django.db import models
from blog.models import Tour
import datetime

class BandMember(models.Model):
    """
    Represents a band member, including their name, role, bio, and image.
    
    Attributes:
        name (str): The name of the band member.
        role (str): The role of the band member (e.g., guitarist, drummer).
        bio (str): A textual biography of the band member.
        image (ImageField): An optional image of the band member.
    """
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='members/')  # Optional for pictures of band members

    def __str__(self):
        """
        Returns the string representation of the band member (their name).
        """
        return self.name


class Album(models.Model):
    """
    Represents a music album by the band.

    Attributes:
        title (str): The title of the album.
        release_date (date): The release date of the album.
        cover_image (ImageField): An image representing the album cover.
        description (str): A textual description of the album.
    """
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='albums/')
    description = models.TextField()

    def __str__(self):
        """
        Returns the string representation of the album (its title).
        """
        return self.title


class Concert(models.Model):
    """
    Represents a concert event.

    Attributes:
        date (date): The date of the concert.
        location (str): The location where the concert is held.
        description (str): A description of the concert event.
    """
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the concert with its location and date.
        """
        return f"{self.location} on {self.date}"


class Band(models.Model):
    """
    Represents a band.

    Attributes:
        name (str): The name of the band.
        genre (str): The genre of music the band plays.
        website (URLField): The band's official website or social media URL.
    """
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    website = models.URLField(blank=True)


class Tour(models.Model):
    """
    Represents a music tour.

    Attributes:
        name (str): The name of the tour.
        start_date (date): The start date of the tour (defaults to today).
        end_date (date): The end date of the tour (defaults to today).
        location (str): The primary location of the tour.
    """
    name = models.CharField(max_length=100)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    location = models.CharField(max_length=200)


print()