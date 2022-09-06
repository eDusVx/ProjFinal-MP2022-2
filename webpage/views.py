from django.shortcuts import render

from .models import Garcon, Prato

def index(request):
    context = {
        'garcons': Garcon.objects.all(),
        'pratos': Prato.objects.all()
    }
    return render(request, 'webpage/index.html', context)
