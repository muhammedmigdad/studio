from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from web.forms import PhotoForm
from .models import Service, WeddingPhotography, Portfolio, GelleryPortfolio, Enquiry, Contact, Filims

@login_required(login_url="login/")
def index(request):
    services = Service.objects.all()
    
    context = {
        "services": services,
    }

    return render(request, 'web/index.html', context=context)


@login_required(login_url="login/")
def about(request):

    return render(request, 'web/about.html')


@login_required(login_url="login/")
def gellery(request):
    photos = WeddingPhotography.objects.all()
    
    context = {
        "photos": photos,
    }

    return render(request, 'web/gellery.html', context=context)

@login_required(login_url="login/")
def filims(request):
    filims = Filims.objects.all()
    
    context = {
        "filims": filims,
    }

    return render(request, 'web/filims.html',  context=context)

@login_required(login_url="login/")
def portfolio(request):
    portfolios = Portfolio.objects.all()
    
    context = {
        
        "portfolios": portfolios,
    }
    return render(request, 'web/portfolio.html', context=context)



@login_required(login_url="login/")
def portfolio_detail(request):
    images = GelleryPortfolio.objects.all()
    
    context = {
        "images": images,
    }

    return render(request, 'web/portfolio-detail.html', context=context)

@login_required(login_url="login/")
def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        location_of_shoot = request.POST.get('location_of_shoot')
        event_date = request.POST.get('EventDate')
        event_address_details = request.POST.get('event_address_details')
        event_type = request.POST.getlist('EventType[]') 

        contact = Contact.objects.create(
            full_name=full_name,
            email=email,
            contact_number=contact_number,
            location_of_shoot=location_of_shoot,
            event_date=event_date,
            event_address_details=event_address_details,
            event_type=", ".join(event_type) 
        )
        contact.save()

        return redirect('web:enquiry')
    else: 
        return render(request, 'web/contact.html')

@login_required(login_url="login/")
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
        
        form = PhotoForm()
        if request.method == 'POST':
            form = PhotoForm(request.POST)
            if form.is_valid():
                subject = 'Code Band'
                message = 'Sending Email through Gmail'
                recipient = form.cleaned_data.get('email')
                send_mail(subject, 
                message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                messages.success(request, 'Success!')

        return HttpResponseRedirect(reverse('web:index'))
    else:  
        return render(request, 'web/enquiry.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(request, username=username, password=password,) 

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('web:index'))
        else:
            context = {
                'error':True,
                'message':'Invalid email or password'
            }
            return render(request, 'web/login.html', context=context)
    else:
        return render(request, 'web/login.html')
    
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(
            first_name=first_name, 
            last_name=last_name,
            username=username,
            password=password,
        )
        user.save()
        return HttpResponseRedirect(reverse('web:login'))
    
    else:
        return render(request, 'web/register.html')
    
    
def logout(request):
   user = request.user
   auth_logout(request)
  
   return HttpResponseRedirect(reverse('web:index'))

