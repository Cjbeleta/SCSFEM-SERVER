from django.shortcuts import render, redirect
import requests
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout as django_logout
from django.http import HttpResponse

# Create your views here.

def landing(request):
    return render(request, 'server/landing.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        url = 'http://localhost:8000/api/user?email=' + request.POST['email']
        response = requests.get(url)
        data = response.json()
        print (data[0]['name'])
        if data:
            request.session['user_id'] = data[0]['id']
            request.session['user_name'] = data[0]['name']
            request.session['user_email'] = data[0]['email']
            request.session['user_type'] = data[0]['usertype']
            request.session['logged_in'] = True
            return HttpResponse(request.session['user_type'])
        else:
            data = {'name': request.POST['fullname'], 'email': request.POST['email'], 'usertype': 2}
            response = requests.post('http://localhost:8000/api/user/', data=data)
            request.session['user_id'] = data[0]['id']
            request.session['user_name'] = data[0]['name']
            request.session['user_email'] = data[0]['email']
            request.session['user_type'] = data[0]['usertype']
            request.session['logged_in'] = True
            return redirect(dashboard)
    else: 
        return redirect(landing)

# @login_required
def logout(request):
    django_logout(request)
    return redirect(landing)


def superadmin_dashboard(request):
    if request.session['logged_in'] and request.session['user_type'] == 0:
        return render(request, 'server/admin_dashboard.html', {'username': request.session['user_name']})
    return redirect(landing)

def subadmin_dashboard(request):
    if request.session['logged_in'] and request.session['user_type'] == 1:
        return render(request, 'server/admin_dashboard.html', {'username': request.session['user_name']})
    return redirect(landing)

def dashboard(request):
    if request.session['logged_in'] and request.session['user_type'] == 2:
        return render(request, 'server/dashboard.html', {'username': request.session['user_name']})
    return redirect(landing)

def facility(request):
    facilities = requests.get('http://localhost:8000/api/facility/')
    return render(request, 'server/facility.html', {'facilities': facilities.json()})

def view_facility(request, pk):
    return render(request, 'server/view_facility.html')

def admin_facility(request):
    facilities = requests.get('http://localhost:8000/api/facility/')
    return render(request, 'server/admin_facility.html', {'facilities': facilities.json()})

def add_facility(request):
    if request.method == 'POST':
        data = {'name': request.POST['name'], 'status': request.POST['status']}
        print (data)
        response = requests.post('http://localhost:8000/api/facility/', data=data)
        print (response)
        return redirect(facility)
    elif request.method == 'GET':
        return render(request, 'server/add_facility.html')

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

def equipment(request):
    equipments = requests.get('http://localhost:8000/api/equipment/')
    return render(request, 'server/equipment.html', {'equipments': equipments.json()})

def add_equipment(request):
    if request.method == 'POST':
        data = {'name': request.POST['name'], 'status': request.POST['status']}
        print (data)
        response = requests.post('http://localhost:8000/api/equipment/', data=data)
        print (response)
        return redirect(equipment)
    elif request.method == 'GET':
        return render(request, 'server/add_equipment.html')

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

def admin_reservation(request):
    return render(request, 'server/admin_reservation.html')

def admin_view_reservation(request, pk):
    return render(request, 'server/admin_reservation.html')

def add_reservation(request):
    if request.method == 'POST':
        data = {'name': request.POST['name'], 'status': request.POST['status']}
        print (data)
        response = requests.post('http://localhost:8000/api/equipment/', data=data)
        print (response)
        return redirect(equipment)
    elif request.method == 'GET':
        return render(request, 'server/add_equipment.html')
