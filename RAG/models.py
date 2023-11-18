from django.db import models

class Carousel(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel_images/')

    def __str__(self):
        return self.title
