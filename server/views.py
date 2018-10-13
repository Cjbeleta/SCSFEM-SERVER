from django.shortcuts import render, redirect
import requests
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def landing(request):
    return render(request, 'server/landing.html')

@csrf_exempt
def dashboard(request):
    return render(request, 'server/dashboard.html')

@csrf_exempt
def facility(request):
    facilities = requests.get('http://localhost:8000/api/facility/')
    return render(request, 'server/facility.html', {'facilities': facilities.json()})

@csrf_exempt
def view_facility(request):
    return render(request, 'server/view_facility.html')

@csrf_exempt
def add_facility(request):
    if request.method == 'POST':
        data = {'name': request.POST['name'], 'status': request.POST['status']}
        print (data)
        response = requests.post('http://localhost:8000/api/facility/', data=data)
        print (response)
        return redirect(facility)
    elif request.method == 'GET':
        return render(request, 'server/add_facility.html')

@csrf_exempt
def edit_facility(request, pk):
    if request.method == 'GET':
        url = 'http://localhost:8000/api/facility/' + pk + '/'
        print (url)
        response = requests.get(url)
        print (response)
        return render(request, 'server/edit_facility.html', {'facility': response.json()})
    elif request.method == 'POST':
        url = 'http://localhost:8000/api/facility/' + pk + '/'
        print (url)
        data = {'name': request.POST['name'], 'status': request.POST['status']}
        print (data)
        edited_facility = requests.put(url, data=data)
        return redirect(facility)

@csrf_exempt
def equipment(request):
    equipments = requests.get('http://localhost:8000/api/equipment/')
    return render(request, 'server/equipment.html', {'equipments': equipments.json()})

@csrf_exempt
def add_equipment(request):
    if request.method == 'POST':
        data = {'name': request.POST['name'], 'status': request.POST['status']}
        print (data)
        response = requests.post('http://localhost:8000/api/equipment/', data=data)
        print (response)
        return redirect(equipment)
    elif request.method == 'GET':
        return render(request, 'server/add_equipment.html')
@csrf_exempt
def edit_equipment(request, pk):
    if request.method == 'GET':
        url = 'http://localhost:8000/api/equipment/' + pk + '/'
        print (url)
        response = requests.get(url)
        print (response)
        return render(request, 'server/edit_equipment.html', {'equipment': response.json()})
    elif request.method == 'POST':
        url = 'http://localhost:8000/api/equipment/' + pk + '/'
        print (url)
        data = {'name': request.POST['name'], 'status': request.POST['status']}
        print (data)
        edited_equipment = requests.put(url, data=data)
        return redirect(equipment)