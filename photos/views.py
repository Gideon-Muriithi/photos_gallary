from django.shortcuts import render

def location (request, location):
    locations = Location.objects.all()
    chosen_location = Location.objects.get(id=location)
    images = Image.objects.filter(location=chosen_location.id)
    context = {
        'location':chosen_location, 'locations':locations, 'images':images
    }
    return render(request, 'location.html',context)
