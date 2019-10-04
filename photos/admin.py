from django.contrib import admin
from . models import Image, Location, categories

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('image_categories',)

admin.site.register(Image, ImageAdmin)
admin.site.register(Location)
admin.site.register(categories,)
