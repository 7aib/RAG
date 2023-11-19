from django.shortcuts import render

from rag_app.models import Carousel

def home(request):
    
    tempelate = 'home.html'
    carousel_items = Carousel.objects.filter(is_active=True)
    data = {
        'carousel_items':carousel_items
        }
    return render(request, tempelate, data)