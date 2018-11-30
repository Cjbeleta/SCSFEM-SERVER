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


def admin_dashboard(request):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            return render(request, 'server/admin_dashboard.html', {'username': request.session['user_name']})
        return redirect(dashboard)
    return redirect(landing)

def dashboard(request):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            return redirect(admin_dashboard)
        return render(request, 'server/dashboard.html', {'username': request.session['user_name']})
    return redirect(landing)

def facility(request):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            return redirect(admin_dashboard)
        facilities = requests.get('http://localhost:8000/api/facility/')
        return render(request, 'server/facility.html', {'facilities': facilities.json()})
    return redirect(landing)

def view_facility(request, pk):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            return redirect(admin_dashboard)
        url = 'http://localhost:8000/api/facility/' + pk + '/'
        response = requests.get(url)
        print (response.json())
        return render(request, 'server/view_facility.html', response.json())
    return redirect(landing)

def view_admin_facility(request, pk):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            url = 'http://localhost:8000/api/facility/' + pk + '/'
            response = requests.get(url)
            print (response.json())
            return render(request, 'server/view_admin_facility.html', response.json())
        return redirect(dashboard)
    return redirect(landing)

def admin_facility(request):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            url = 'http://localhost:8000/api/facility/'
            facilities = requests.get(url)
            return render(request, 'server/admin_facility.html', {'facilities': facilities.json()})
        return redirect(dashboard)
    return redirect(landing)

def add_facility(request):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            if request.method == 'POST':
                data = {'name': request.POST['name'], 'status': request.POST['status']}
                print (data)
                response = requests.post('http://localhost:8000/api/facility/', data=data)
                print (response)
                return redirect(admin_facility)
            elif request.method == 'GET':
                return render(request, 'server/add_facility.html')
        return redirect(dashboard)
    return redirect(landing)

def edit_facility(request, pk):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            if request.method == 'POST':
                url = 'http://localhost:8000/api/facility/' + pk + '/'
                print (url)
                data = {'name': request.POST['name'], 'status': request.POST['status']}
                print (data)
                edited_facility = requests.put(url, data=data)
                return redirect(admin_facility)
        return redirect(dashboard)
    return redirect(landing)

def equipment(request):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            return redirect(admin_dashboard)
        equipments = requests.get('http://localhost:8000/api/equipment/')
        return render(request, 'server/equipment.html', {'equipments': equipments.json()})
    return redirect(landing)

def admin_equipment(request):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            equipments = requests.get('http://localhost:8000/api/equipment/')
            return render(request, 'server/admin_equipment.html', {'equipments': equipments.json()})
        return redirect(dashboard)
    return redirect(landing)

def view_admin_equipment(request, pk):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            equipment = requests.get('http://localhost:8000/api/equipment/' + pk + '/')
            return render(request, 'server/view_admin_equipment.html', equipment.json())
        return redirect(dashboard)
    return redirect(landing)

def add_equipment(request):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            if request.method == 'POST':
                data = {'name': request.POST['name'], 'status': request.POST['status']}
                print (data)
                response = requests.post('http://localhost:8000/api/equipment/', data=data)
                print (response)
                return redirect(admin_equipment)
        return redirect(dashboard)
    return redirect(landing)

def edit_equipment(request, pk):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            if request.method == 'POST':
                url = 'http://localhost:8000/api/equipment/' + pk + '/'
                print (url)
                data = {'name': request.POST['name'], 'status': request.POST['status']}
                print (data)
                edited_equipment = requests.put(url, data=data)
                return redirect(admin_equipment)
        return redirect(dashboard)
    return redirect(landing)

def admin_reservation(request):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            url = 'http://localhost:8000/api/reservation/'
            response = requests.get(url)
            print (response)
            return render(request, 'server/admin_reservation.html', {'reservation': response.json()})
        return redirect(dashboard)
    return redirect(landing)

def apply_reservation(request, pk):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            return redirect(admin_dashboard)
        if request.method == 'POST':
            data = {
            'borrower_id': request.POST['borrower_id'],
            'item_id': request.POST['item_id'],
            'reservation_type': request.POST['reservation_type'],
            'date_application': request.POST['date_application'],
            'date_reservation_start': request.POST['date_reservation_start'],
            'date_reservation_end': request.POST['date_reservation_end'],
            'status': request.POST['status']}
            print (data)
            response = requests.post('http://localhost:8000/api/reservation/', data=data)
            print (response)
            return redirect(dashboard)
        elif request.method == 'GET':
            return render(request, 'server/reservation.html')
    return redirect(landing)
