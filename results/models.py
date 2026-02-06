from django.db import models

# Create your models here.

class certificate(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='certificates/')
    
    def __str__(self):
        return self.title