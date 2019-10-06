from django.shortcuts import render
from . models import Location, Image, categories


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

def seach_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        searched_images = Image.search_by_category((search_term))
        message = f"{search_term}"
        context = {"message":message,"images":searched_images,
            "category":search_term
        }
        return render(request, 'search.html', context)
    else:
        message = "You haven't searched for any category!"
        return render(request, 'search.html',{"message":message})
