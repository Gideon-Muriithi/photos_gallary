from django.db import models

class Image(models.Model):
    image = models.ImageField(default='default.jpg' upload_to = 'pictures/')
    image_name = models.CharField(max_length=30,default="Title")
    image_description = models.TextField()
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ManyToManyField(category)

    def __str__(self):
        return self.image_name