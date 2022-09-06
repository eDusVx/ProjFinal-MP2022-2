from django.shortcuts import render

from .models import Garcon

def index(request):
    context = {
        'garcon': Garcon.objects.all()
    }
    return render(request, 'webpage/index.html', context)
