from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from random import randrange
from .models import Ins
from myapp.models import Complaint
# Create your views here.
#registration
data = {}  # Global variable to store registration data

def register_station(request):
    if request.method == 'POST':
        try:
            Ins.objects.get(email=request.POST['email'])
            msg = 'Email already exists'
            return render(request, 'station_register.html', {'msg': msg})
        except Ins.DoesNotExist:
            if request.POST['password'] == request.POST['rpassword']:
                otp = randrange(1000, 9999) 
                print(otp)  
                subject = 'ONE TIME PASSWORD FOR USER REGISTRATION'
                message = f'{otp} please paste this number in the OTP field to verify your account.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail(subject, message, email_from, recipient_list)
                
                global data 
                data = {
                    'password': request.POST['password'],
                    'email': request.POST['email'],
                    'station_name': request.POST['station_name'],
                    'station_id': request.POST['station_id'],
                    'address': request.POST['address'],
                    'phone': request.POST['phone'],
                }
                
                return render(request, 'ins-otp.html', {'msg': 'OTP sent', 'otp': otp})
            
            return render(request, 'station_register.html', {'msg': 'Both passwords are not the same'})
    
    return render(request, 'station_register.html')


def otp_stationn(request):
    if request.method == 'POST':
        if request.POST['otp'] == request.POST['uotp']:
            global data
            Ins.objects.create(
                password=data['password'],
                email=data['email'],
                station_name=data['station_name'],
                station_id=data['station_id'],
                address=data['address'],
                phone=data['phone'],
            )
            return render(request, 'ins-login.html', {'msg': 'Station Created'})
        
        return render(request, 'ins-otp.html', {'msg': 'Invalid OTP', 'otp': request.POST['otp']})
    
    return render(request, 'ins-login.html')

def ins_login(request):
    if request.method == 'POST':
        try:
            ins = Ins.objects.get(email=request.POST['email'])
            if request.POST['password'] == ins.password:
                request.session['email'] = request.POST['email']
                return redirect('ins-index')
            return render(request,'ins-login.html',{'msg':'Incorrect Password'})
        except:
            msg = 'Account not registered' 
            return render(request,'ins-login.html',{'msg':msg})
    return render(request,'ins-login.html')

def ins_index(request):
    ins = Ins.objects.get(email=request.session['email'])
    return render(request,'ins-index.html',{'ins':ins})

def ins_view_FIR(request):
    ins = Ins.objects.get(email=request.session['email'])
    FIRs= FIR.objects.all()
    return render(request,'ins-view-FIR.html',{'ins':ins,'FIRs':FIRs})

def ins_view_one_FIR(request,pk):
    ins = Ins.objects.get(email=request.session['email'])
    fir=FIR.objects.get(id=pk)
    return render(request, 'ins-view-one-FIR.html',{'ins':ins,'fir':fir})

def ins_view_com(request):
    ins = Ins.objects.get(email=request.session['email'])
    com=Complaint.objects.all()
    return render(request,'ins-view-com.html',{'ins':ins,'com':com})

def ins_view_one_com(request,pk):
    ins = Ins.objects.get(email=request.session['email'])
    com=Complaint.objects.get(id=pk)
    return render(request, 'ins-view-one-com.html',{'ins':ins,'com':com})

def ins_manage_com(request):
    ins = Ins.objects.get(email=request.session['email'])
    com=Complaint.objects.all()
    return render(request,'ins-manage-com.html',{'ins':ins,'com':com})

def ins_disable(request,pk):
    ins = Ins.objects.get(email=request.session['email'])
    com=Complaint.objects.get(id=pk)
    com.status = False
    com.save()
    return redirect('ins-manage-com')

def ins_enable(request,pk):
    ins = Ins.objects.get(email=request.session['email'])
    com=Complaint.objects.get(id=pk)
    com.status = True
    com.save()
    return redirect('ins-manage-com')

def ins_manage_view(request,pk):
    ins = Ins.objects.get(email=request.session['email'])
    com=Complaint.objects.get(id=pk)
    return render(request, 'ins-manage-view.html',{'ins':ins,'com':com})

def ins_edit_profile(request):
    ins = Ins.objects.get(email=request.session['email'])
    if request.method == 'POST':
        ins.fname = request.POST['fname']
        ins.lname = request.POST['lname']
        
        if 'pic' in request.FILES:
            ins.pic = request.FILES['pic']
        ins.save()
    return render(request,'ins-eprofile.html',{'ins':ins})

def ins_view_profile(request):
    ins = Ins.objects.get(email=request.session['email'])
    return render(request,'ins-view-profile.html',{'ins':ins})

def ins_password(request):
    ins = Ins.objects.get(email=request.session['email'])
    if request.method == 'POST':
        if request.POST['opassword'] == ins.password:
            if request.POST['password'] == request.POST['rpassword']:
                ins.password = request.POST['password']
                ins.save()
                return render(request,'ins-password.html',{'ins':ins,'msg':'Password has been changed'})
            return render(request,'ins-password.html',{'ins':ins,'msg':'New entered password are different'})
        return render(request,'ins-password.html',{'ins':ins,'msg':'Old Password is incorrect'})
    return render(request,'ins-password.html',{'ins':ins})

from .models import MostWanted

def add_most_wanted(request):
    if request.method == 'POST':
        # Retrieve form data
        full_name = request.POST.get('full_name')
        alias = request.POST.get('alias')
        date_of_birth = request.POST.get('date_of_birth')
        place_of_birth = request.POST.get('place_of_birth')
        gender = request.POST.get('gender')
        nationality = request.POST.get('nationality')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        eye_color = request.POST.get('eye_color')
        hair_color = request.POST.get('hair_color')
        distinguishing_features = request.POST.get('distinguishing_features')
        offenses_committed = request.POST.get('offenses_committed')
        last_known_location = request.POST.get('last_known_location')
        rewards_offered = request.POST.get('rewards_offered')
        recent_photographs = request.FILES.get('recent_photographs')
        contact_numbers = request.POST.get('contact_numbers')
        background_information = request.POST.get('background_information')
        known_addresses = request.POST.get('known_addresses')
        date_of_last_known_activity = request.POST.get('date_of_last_known_activity')
        current_status = request.POST.get('current_status')

        # Create MostWanted object
        MostWanted.objects.create(
            full_name=full_name,
            alias=alias,
            date_of_birth=date_of_birth,
            place_of_birth=place_of_birth,
            gender=gender,
            nationality=nationality,
            height=height,
            weight=weight,
            eye_color=eye_color,
            hair_color=hair_color,
            distinguishing_features=distinguishing_features,
            offenses_committed=offenses_committed,
            last_known_location=last_known_location,
            rewards_offered=rewards_offered,
            recent_photographs=recent_photographs,
            contact_numbers=contact_numbers,
            background_information=background_information,
            known_addresses=known_addresses,
            date_of_last_known_activity=date_of_last_known_activity,
            current_status=current_status
        )

        messages.success(request, 'Details added successfully!')


        # Redirect to a success page or wherever you want
        return redirect('ins-index')

    return render(request, 'ins-mostwanted.html')

def most_wanted_list(request):
    most_wanted_list = MostWanted.objects.all()
    return render(request, 'ins-view_most_wanted.html', {'most_wanted_list': most_wanted_list})

def view_most_wanted(request, pk):
    person = get_object_or_404(MostWanted, pk=pk)
    return render(request, 'ins-one-mostwanted.html', {'person': person})

def edit_most_wanted(request, pk):
    person = get_object_or_404(MostWanted, pk=pk)
    if request.method == 'POST':
        person.full_name = request.POST.get('full_name')
        # Update other fields here
        person.save()
        return redirect('most_wanted_list')
    return render(request, 'ins-edit_mw.html', {'person': person})

def delete_most_wanted(request, pk):
    person = get_object_or_404(MostWanted, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('most_wanted_list')
    return render(request, 'ins-confirm_delete.html', {'person': person})