from django.db import models

class Tour(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.location} on {self.date}"
    

class Grammy(models.Model):
    award_year = models.IntegerField()
    category = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.award_year} - {self.category}"
