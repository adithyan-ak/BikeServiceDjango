
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User, auth
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from django.core.mail import send_mail
from .forms import SignUpForm
from .models import Servicetype, Service


def index(request):
	return render(request, 'index.html')

def dashboard(request):

    if request.method == 'GET':

        services = list(Servicetype.objects.values())
        return render(request, 'dashboard.html', {'services':services})

def service(request):
    
    if request.method == 'GET':

        services = list(Service.objects.values().filter(user=request.user))

        return render(request, 'service.html',{'services':services})

    if request.method == 'POST':
        stype = request.POST['stype']

        vehiclenum = request.POST['vehiclenum']

        manufacturer = request.POST['manufacturer']

        servicedate = request.POST['servicedate']

        serviceupdate = Service()
        serviceupdate.servicedate = servicedate
        serviceupdate.stype = stype
        serviceupdate.vehiclenum = vehiclenum
        serviceupdate.manufacturer = manufacturer
        serviceupdate.user = request.user
        serviceupdate.save()

        message = "Hello "+request.user.get_full_name()+", We are pleased to inform you that the Bike service for "+vehiclenum+" has been scheduled on "+servicedate

        send_mail('Bike Service Scheduled', message, 'johnbikeservice@gmail.com', [request.user.email], fail_silently=False)

        ownermessage = "A new Bike service request has been booked by "+request.user.get_full_name()+" for "+vehiclenum+" scheduled to be delivered on "+servicedate
        send_mail('New Bike Service Booking', ownermessage, 'johnbikeservice@gmail.com', ['johnbikeservice@gmail.com'], fail_silently=False)


        services = list(Service.objects.values().filter(user=request.user))

        return render(request, 'service.html',{'services':services, 'success':'success'})


def Login(request):
    if request.method == 'GET':
	    return render(request, 'login.html')

    if request.method == 'POST':

        username = request.POST['uname']

        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'Auth': 'False'})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("login")


