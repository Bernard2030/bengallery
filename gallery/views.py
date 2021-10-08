from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Location, Category

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"images": searched_image})

    else:
        message = "You haven't searched for any image category"
        return render(request, 'all-gallery/search.html',{"message":message})    