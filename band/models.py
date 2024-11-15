from django.db import models

class BandMember(models.Model):
    """
    Represents a band member, including their name, role, bio, and image.
    
    Attributes:
        name: The name of the band member.
        role: The role of the band member (e.g., guitarist, drummer).
        bio: A textual biography of the band member.
        image: An optional image of the band member.
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
    Represents a music album by the band, including the title, release date, cover image, and description.
    
    Attributes:
        title: The title of the album.
        release_date: The release date of the album.
        cover_image: An image representing the album cover.
        description: A textual description of the album.
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
    Represents a concert event, including the date, location, and description.
    
    Attributes:
        date: The date of the concert.
        location: The location where the concert is held.
        description: A description of the concert event.
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
    Represents the band itself, including the name, genre, and website URL.
    
    Attributes:
        name: The name of the band.
        genre: The genre of music the band plays.
        website: The band's official website or social media URL.
    """
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    website = models.URLField(blank=True)

