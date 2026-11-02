
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Car

def home(request):
    cars = Car.objects.all().order_by('-created_at')

    search = request.GET.get('search', '')
    brand = request.GET.get('brand', '')
    fuel = request.GET.get('fuel', '')
    max_price = request.GET.get('max_price', '')

    if search:
        cars = cars.filter(
            Q(brand__icontains=search) |
            Q(model__icontains=search)
        )

    if brand:
        cars = cars.filter(brand=brand)

    if fuel:
        cars = cars.filter(fuel=fuel)

    if max_price:
        try:
            cars = cars.filter(price__lte=max_price)
        except (ValueError, TypeError):
            pass

    context = {
        'cars': cars,
        'brands': Car.objects.values_list('brand', flat=True).distinct(),
        'fuels': Car.objects.values_list('fuel', flat=True).distinct(),
        'search': search,
        'selected_brand': brand,
        'selected_fuel': fuel,
        'max_price': max_price,
    }

    return render(request, 'cars/home.html', context)


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)

    return render(request, 'cars/detail.html', {
        'car': car
    })
