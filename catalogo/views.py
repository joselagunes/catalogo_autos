from django.shortcuts import render, get_object_or_404
from .models import Car
from category.models import Category
#from django.http import HttpResponse

# Create your views here.
def catalogo(request, category_slug=None):
    categories = None
    cars = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        cars = Car.objects.filter(category=categories, is_available=True)
        #car_count = cars.count()
    else:
        cars = Car.objects.all().filter(is_available=True)
        #car_count =

    context = {
        'cars' : cars,
    }

    return render(request, 'catalogo/catalogo.html', context)

def car_detail(request, category_slug, car_slug):
    try:
        single_car = Car.objects.get(category__slug=category_slug,
                                    slug=car_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_car': single_car,
    }

    return render(request, 'catalogo/car_detail.html', context)


