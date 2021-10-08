from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image, Location, Category
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.



def Home(request):
    category = Category.get_category()
    location = Location.get_location()
    return render(request,'photos.html',{'category':category, 'location':location})




def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_image})

    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html',{"message":message})  

def single_image(request,id):
    try:
        photo = Image.objects.get(id = id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"single_image.html", {"photo":photo}) 

def search_by_location(request,location):
    image_location = Image.filter_image_by_location(location)
    
    return render(request,"location_photos.html", {"image_location":image_location})  


def search_by_category(request,category):
    image_category= Image.get_category(category)
    
    return render(request,"category.html", {"image_category":image_category})           

            