from django.shortcuts import render, redirect
import requests
import datetime
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
        # url = 'http://localhost:8000/api/user?email=' + request.POST['email']
        # response = requests.get(url)
        # data = response.json()
        # print (data[0]['name'])
        # if data:
        #     request.session['user_id'] = data[0]['id']
        #     request.session['user_name'] = data[0]['name']
        #     request.session['user_email'] = data[0]['email']
        #     request.session['user_type'] = data[0]['usertype']
        #     request.session['logged_in'] = True
        #     return HttpResponse(request.session['user_type'])
        # else:
        #     data = {'name': request.POST['fullname'], 'email': request.POST['email'], 'usertype': 2}
        #     response = requests.post('http://localhost:8000/api/user/', data=data)
        #     request.session['user_id'] = data[0]['id']
        #     request.session['user_name'] = data[0]['name']
        #     request.session['user_email'] = data[0]['email']
        #     request.session['user_type'] = data[0]['usertype']
        #     request.session['logged_in'] = True
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
    request.session['user_id'] = 3
    request.session['user_name'] = 'Trisha Mae P. Beleta'
    request.session['user_email'] = 'trishamae.beleta@g.msuiit.edu.ph'
    request.session['user_type'] = 2
    request.session['logged_in'] = True

    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            return redirect(admin_dashboard)
        user = request.session['user_id']
        return render(request, 'server/dashboard.html', {'username': request.session['user_name'], 'date_today': datetime.datetime.today().strftime('%m-%d-%Y')})
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
        return render(request, 'server/view_facility.html', {'facility': response.json()})
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

def view_equipment(request, pk):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            return redirect(admin_dashboard)
        url = 'http://localhost:8000/api/equipment/' + pk + '/'
        response = requests.get(url)
        equipment = response.json()
        return render(request, 'server/view_equipment.html', {'equipment': equipment})
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
                data = {'name': request.POST['name'], 'quantity': request.POST['quantity'], 'status': request.POST['status']}
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
            current_day = int(datetime.datetime.today().strftime('%d'))
            current_month = int(datetime.datetime.today().strftime('%m'))
            print(current_month)
            print(current_day)
            url = 'http://localhost:8000/api/reservation/'
            response = requests.get(url)
            print (response)
            return render(request, 'server/admin_reservation.html', {'reservation': response.json(), 'current_month': current_month, 'current_day': current_day})
        return redirect(dashboard)
    return redirect(landing)

def approve_reservation(request, pk):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            url = 'http://localhost:8000/api/reservation/' + pk
            response = requests.get(url)
            reservation = response.json()
            print(reservation)
            url = 'http://localhost:8000/api/reservation/' + pk + '/'
            data = {'status': 1, 'borrower_id': reservation['borrower_id'], 'item_id': reservation['item_id']}
            response = requests.put(url, data=data)
            print (data)
            return redirect(admin_reservation)
        return redirect(dashboard)
    return redirect(landing)

def reject_reservation(request, pk):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            url = 'http://localhost:8000/api/reservation/' + pk
            response = requests.get(url)
            reservation = response.json()
            print(reservation)
            url = 'http://localhost:8000/api/reservation/' + pk + '/'
            data = {'status': 2, 'borrower_id': reservation['borrower_id'], 'item_id': reservation['item_id']}
            response = requests.put(url, data=data)
            print (data)
            return redirect(admin_reservation)
        return redirect(dashboard)
    return redirect(landing)
 
def apply_reservation(request, pk):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            return redirect(admin_dashboard)
        if request.method == 'POST':
            print(request.POST['type'])
            if request.POST['type'] == str(0):
                data = {
                'borrower_id': request.session['user_id'],
                'item_id': pk,
                'reserve_type': 'facility',
                'eventname': request.POST['eventname'],
                'year': 2018,
                'month': request.POST['month'],
                'start_day': request.POST['start_day'],
                'end_day': request.POST['end_day'],
                'start_time': request.POST['start_time'],
                'end_time': request.POST['end_time']
                }
                print (data)
                response = requests.post('http://localhost:8000/api/reservation/', data=data)
                print (response)
                return redirect(view_facility, pk)
            elif request.POST['type'] == str(1):
                data = {
                    'borrower_id': request.session['user_id'],
                    'item_id': pk,
                    'reserve_type': 'equipment',
                    'quantity': request.POST['quantity'],
                    'year': 2018,
                    'month': request.POST['month'],
                    'start_day': request.POST['start_day'],
                    'end_day': request.POST['end_day'],
                    'start_time': request.POST['start_time'],
                    'end_time': request.POST['end_time']
                }
                print (data)
                response = requests.post('http://localhost:8000/api/reservation/', data=data)
                print (response)
                return redirect(view_equipment, pk)
            return redirect(facility)
        return redirect(dashboard)
    return redirect(landing)

def reservation_list(request):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            return redirect(admin_dashboard)
        url = 'http://localhost:8000/api/reservation?user=' + str(request.session['user_id'])
        response = requests.get(url)
        reservation = response.json()
        return render(request, 'server/reservation.html', {'reservation': reservation})
    return redirect(landing)

def edit_reservation(request, pk):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            return redirect(admin_dashboard)
        if request.method == 'POST':
            if request.POST['type'] == 'facility':
                data = {
                    'borrower_id': request.session['user_id'],
                    'item_id': request.POST['item_id'],
                    'eventname': request.POST['eventname'],
                    'month': request.POST['month'],
                    'start_day': request.POST['start_day'],
                    'end_day': request.POST['end_day'],
                    'start_time': request.POST['start_time'],
                    'end_time': request.POST['end_time']
                }
            else:
                data = {
                    'borrower_id': request.session['user_id'],
                    'item_id': request.POST['item_id'],
                    'quantity': request.POST['quantity'],
                    'month': request.POST['month'],
                    'start_day': request.POST['start_day'],
                    'end_day': request.POST['end_day'],
                    'start_time': request.POST['start_time'],
                    'end_time': request.POST['end_time'],
                }
            print(data)
            url = 'http://localhost:8000/api/reservation/' + pk + '/'
            response = requests.put(url, data=data)
            print(response)
            return redirect(reservation_list)
        return redirect(dashboard)
    return redirect(landing)

def delete_reservation(request, pk):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            return redirect(admin_dashboard)
        url = 'http://localhost:8000/api/reservation/' + pk
        response = requests.delete(url)
        return redirect(reservation_list)
    return redirect(landing)

def check_reservation(request, pk):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            if request.method == 'POST':
                url = 'http://localhost:8000/api/reservation/' + pk
                response = requests.get(url)
                reservation = response.json()
                url = 'http://localhost:8000/api/reservation/' + pk + '/'
                data = {
                    'borrower_id': reservation['borrower_id'],
                    'item_id': reservation['item_id'],
                    'remarks': request.POST['remarks'],
                    'status': 3
                }
                response = requests.put(url, data=data)
                return redirect(admin_reservation)
            return redirect(admin_dashboard)
        return redirect(dashboard)
    return redirect(landing)

def users(request):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            url = 'http://localhost:8000/api/user/'
            response = requests.get(url)
            users = response.json()
            return render(request, 'server/user.html', {'users': users})
        return redirect(dashboard)
    return redirect(landing)

def change_user_type(request, pk):
    if request.session['logged_in']:
        if request.session['user_type'] == 0 or request.session['user_type'] == 1:
            if request.method == 'POST':
                url = 'http://localhost:8000/api/user/' + pk
                response = requests.get(url)
                user = response.json()
                url = 'http://localhost:8000/api/user/' + pk + '/'
                data = {
                    'name': user['name'],
                    'email': user['email'],
                    'usertype': request.POST['usertype']
                }
                response = requests.put(url, data=data)
                return redirect(users)
            return redirect(admin_dashboard)
        return redirect(dashboard)
    return redirect(landing)