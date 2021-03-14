from django.db import models

# Create your models here.

# Class for the image directory zips
class Images(models.Model):
    title = models.CharField(max_length = 100)
    img_zip = models.FileField(upload_to = 'media/images/')

    def __str__(self):
        return self.title
