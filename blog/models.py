"""
Defines database models for the Blog application.
"""

from django.db import models

class Tour(models.Model):
    """
    Represents a music tour event, including the name, location, and date.

    Attributes:
        name (str): The name of the tour.
        location (str): The location where the tour is held.
        date (date): The date of the tour event.
    """

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        """
        Returns a string representation of the tour event.
        """
        return f"{self.name} - {self.location} on {self.date}"
    

class Grammy(models.Model):
    """
    Represents a Grammy award, including the year, category, and description.

    Attributes:
        award_year (int): The year the Grammy was awarded.
        category (str): The award category.
        description (str): A brief description of the award.
    """

    award_year = models.IntegerField()
    category = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the Grammy award.
        """
        return f"{self.award_year} - {self.category}"


print()

