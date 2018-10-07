from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'server/home.html')

def facility(request):
    content = {'facilities' : [{'name': 'Facility A'}, {'name': 'Facility B'}]}
    return render(request, 'server/facility.html', {'content': content})

def equipment(request):
    content = {'equipments': [{'name': 'Equipment A'}, {'name': 'Equipment B'}]}
    return render(request, 'server/equipment.html', {'content': content})
