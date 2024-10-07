from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from web.models import Enquiry
from django.contrib import messages
from manager.forms import *
from main.functions import generate_form_errors
from main.decorators import allow_manager


def login(request):
    if request.method == "POST":
        form = ManagerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_manager: 
                    auth_login  (request,user)
                    return redirect('manager:index') 
                else:
                    messages.error(request, "Unauthorized access.")
                    return HttpResponse("unauthorized", status=401)
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Form is invalid.")
    else:
        form = ManagerLoginForm()

    return render(request, 'manager/login.html', {'form': form})

def logout(request):
    return redirect('manager:login')
@allow_manager
@login_required(login_url='/login/')

def enquiry(request):
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        enquiry_number = request.POST.get('enquiry_number')
        location_of_shoot = request.POST.get('location_of_shoot')
        event_date = request.POST.get('EventDate')
        event_address_details = request.POST.get('event_address_details')
        event_type = request.POST.getlist('EventType[]') 

        enquiry = Enquiry.objects.create(
            full_name=full_name,
            email=email,
            enquiry_number=enquiry_number,
            location_of_shoot=location_of_shoot,
            event_date=event_date,
            event_address_details=event_address_details,
            event_type=", ".join(event_type) 
        )
        enquiry.save()

        return HttpResponseRedirect(reverse('web:contact'))
    else:  
        return render(request, 'manager/index.html')



