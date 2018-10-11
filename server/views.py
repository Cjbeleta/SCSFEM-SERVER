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
    print (facilities.json())
    content = {'facilities' : facilities.json()}
    return render(request, 'server/facility.html', {'content': content})
@csrf_exempt
def view_facility(request):
    return render(request, 'server/view_facility.html')
@csrf_exempt
def add_facility(request):
    if request.method == 'POST':
        data = {'data': [{'name': request.POST['name'], 'status': request.POST['status']}]}
        requests.post('http://localhost:8000/api/facility/', data)
        return redirect(facility)
    elif request.method == 'GET':
        return render(request, 'server/add_facility.html')
@csrf_exempt
def edit_facility(request):
    return render(request, 'server/edit_facility.html')
@csrf_exempt
def equipment(request):
    content = {'equipments': [{'name': 'Equipment A'}, {'name': 'Equipment B'}]}
    return render(request, 'server/equipment.html', {'content': content})
