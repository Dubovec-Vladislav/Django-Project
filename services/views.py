from django.shortcuts import render


def food(request):
    return render(request, 'services/food.html')


def fashion(request):
    return render(request, 'services/fashion.html')


def booking(request):
    return render(request, 'services/booking.html')


def marketing(request):
    return render(request, 'services/marketing.html')


def design(request):
    return render(request, 'services/design.html')


def making_food(request):
    return render(request, 'services/making_food.html')
