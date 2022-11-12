from django.shortcuts import render
from catalogo.models import Car

def home(request):

    cars = Car.objects.all().filter(is_available=True)

    context = {
        'cars': cars,
    }

    return render(request, 'home.html', context)

