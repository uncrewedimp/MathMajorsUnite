from django.db import models

# Create your models here.

# Class for the image directory zips
class Images(models.Model):
    title = models.CharField(max_length = 100)
    img_zip = models.FileField(upload_to = 'media/images/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Makes sure this class deletes the file from local storage
        self.img_zip.delete()
        super().delete(*args, **kwargs)

class Text(models.Model):
    title = models.CharField(max_length = 100)
    txt = models.FileField(upload_to = 'media/text/')

    rows = models.PositiveIntegerField(default = 0)
    cols = models.PositiveIntegerField(default = 0)

    # Records date that data was added:
    added = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Makes sure this class deletes the file from local storage
        self.txt.delete()
        super().delete(*args, **kwargs)
