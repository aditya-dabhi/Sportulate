from django.db import models


# Create your models here.
class CricTeam(models.Model):
    name = models.CharField(max_length=100)
    primary_color_name = models.CharField(max_length=100)
    primary_color_code = models.CharField(max_length=100)
    secondary_color_name = models.CharField(max_length=100)
    secondary_color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.name
