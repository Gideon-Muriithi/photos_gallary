from django.shortcuts import render
from . models import Location, Image


def get_images(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    context = { "images":images,
        "locations":locations
    }
    return render(request, 'images.html', context)


def get_location (request, location):
    locations = Location.objects.all()
    chosen_location = Location.objects.get(id=location)
    images = Image.objects.filter(location=chosen_location.id)
    context = {
        'location':chosen_location, 'locations':locations, 'images':images
    }
    return render(request, 'location.html',context)

