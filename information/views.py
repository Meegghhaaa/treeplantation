from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'info/index.html')

def indoor(request):
    return render(request, 'info/indoor.html')

def outdoor(request):
    return render(request, 'info/outdoor.html')

def tools(request):
    return render(request, 'info/tools.html')

def page_open_lemon(request):
    return render(request, 'indoor_plants/lemon.html')

def page_open_chilly(request):
    return render(request, 'indoor_plants/chilly.html')

def page_open_curry(request):
    return render(request, 'indoor_plants/curry.html')

def page_open_plumbago(request):
    return render(request, 'outdoor_plants/plumbago.html')

def page_open_ajuga(request):
    return render(request, 'outdoor_plants/ajuga.html')

def page_open_trowel(request):
    return render(request, 'gardening_tools/trowel.html')