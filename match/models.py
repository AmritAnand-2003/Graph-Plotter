from django.db import models

# Create your models here.


class matches(models.Model):
    season = models.CharField(max_length = 200)
    winner = models.CharField(max_length = 200)
    def __str__(self):
        return self.winner
    
class match(models.Model):
    season = models.CharField(max_length = 200)
    winner = models.CharField(max_length = 200)
    def __str__(self):
        return self.winner
    
class school(models.Model):
    district = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    language = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name
    
