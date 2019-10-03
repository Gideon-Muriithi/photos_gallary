from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delte_location(self):
        self.delete()

class categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_categories(self):
        self.save()

    def delete_categories(self):
        self.delete()    


class Image(models.Model):
    image = models.ImageField(default='default.jpg' upload_to = 'pictures/')
    image_name = models.CharField(max_length=30,default="Title")
    image_description = models.TextField()
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_categories = models.ManyToManyField(categories)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()