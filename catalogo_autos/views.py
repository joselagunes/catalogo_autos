from django.shortcuts import render
from catalogo.models import Car

def home(request):

    car = Car.objects.all().filter(is_available=True)

    context = {
        'car': car,
    }

    return render(request, 'home.html', context)

