from django.shortcuts import render

from cars.models import Car
# Create your views here.

def cars_view(request):
    search = request.GET
    cars = Car.objects.all()
    print(search)
    return render(
        request, 'cars.html',
        context = {
            'cars' : cars,
        }
    )
    
    # <QueryDict: {'search': ['mare']}>