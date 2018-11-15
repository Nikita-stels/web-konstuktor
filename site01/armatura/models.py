from django.db import models

# Create your models here.

class sortam_armatura (models.Model):
    Dim = models.CharField(max_length=3)
    Ves = models.CharField(max_length=5)
    Plosh = models.CharField(max_length=5)

    def __str__(self):
        return self.Dim



