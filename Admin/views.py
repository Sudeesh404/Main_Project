from ast import Pass
from re import sub
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from Inspector.models import Ins, Sub
from . models import *
from myapp.models import Missing, Feedback, Complaint

# Create your views here.

def admin_index(request):
    adm = Admin.objects.get(email=request.session['email'])
    return render(request,'admin-index.html',{'adm':adm})

from myapp.models import User, Station  # Import necessary models

def admin_dashboard(request):
    user_count = User.objects.all().count()
    # ... You can continue with other counts if needed
    station_count = Ins.objects.all().count()
    missing_count = Missing.objects.all().count()
    feedback_count = Feedback.objects.all().count()
    complaint_count = Complaint.objects.all().count()

    context = {
        'user_count': user_count,
        # Add other counts here
        'station_count': station_count,
        'missing_count':missing_count,
        'feedback_count':feedback_count,
        'complaint_count':complaint_count,
    }

    return render(request, 'admin-dashboard.html', context)

def admin_login(request):
    if request.method == 'POST':
        try:
            adm = Admin.objects.get(email=request.POST['email'])
            if request.POST['password'] == adm.password:
                request.session['email'] = request.POST['email']
                return redirect('admin-index')
            return render(request,'admin-login.html',{'msg':'Incorrect Password'})
        except:
            msg = 'Account not registered' 
            return render(request,'admin-login.html',{'msg':msg})
    return render(request,'admin-login.html')

def admin_logout(request):
   del request.session['email']
   return redirect('index') 

def admin_view_FIR(request):
    adm = Admin.objects.get(email=request.session['email'])
    FIRs= FIR.objects.all()
    return render(request,'admin-view-FIR.html',{'adm':adm,'FIRs':FIRs})

def admin_view_one_FIR(request,pk):
    adm = Admin.objects.get(email=request.session['email'])
    fir=FIR.objects.get(id=pk)
    return render(request, 'admin-view-one-FIR.html',{'adm':adm,'fir':fir})

def admin_station(request):
    adm = Admin.objects.get(email=request.session['email'])
    stations= Station.objects.all()
    return render(request, 'admin-station.html',{'adm':adm,'stations':stations})

def admin_one_station(request,pk):
    adm = Admin.objects.get(email=request.session['email'])
    stations= Station.objects.get(id=pk)
    if request.method == 'POST':
        stations.station = request.POST['station']
        stations.address = request.POST['address']
        if 'img' in request.FILES:
            stations.img = request.FILES['img']
        
        stations.save()
    return render(request, 'admin-one-station.html',{'adm':adm,'stations':stations})

def admin_user(request):
    adm = Admin.objects.get(email=request.session['email'])
    uid=User.objects.all()
    return render(request,'admin-user.html',{'adm':adm,'uid':uid})

def admin_one_user(request,pk):
    adm = Admin.objects.get(email=request.session['email'])
    uid = User.objects.get(id=pk)
    if request.method == 'POST':
        uid.fname = request.POST['fname']
        uid.lname = request.POST['lname']
        uid.phone = request.POST['phone']
        
        
        uid.save()
    return render(request, 'admin-one-user.html',{'adm':adm,'uid':uid})

def admin_policestation(request):
    adm = Admin.objects.get(email=request.session['email'])
    ins= Ins.objects.all()
    return render(request,'admin-policestation.html',{'adm':adm,'ins':ins})

def admin_one_ins(request,pk):
    adm = Admin.objects.get(email=request.session['email'])
    ins = Ins.objects.get(id=pk)
    if request.method == 'POST':
        ins.fname = request.POST['fname']
        ins.lname = request.POST['lname']
        ins.user_id = request.POST['user_id']
        if 'pic' in request.FILES:
            ins.pic = request.FILES['pic']
        
        ins.save()
    return render(request, 'admin-one-ins.html',{'adm':adm,'ins':ins})

def admin_subins(request):
    adm = Admin.objects.get(email=request.session['email'])
    sub= Sub.objects.all()
    return render(request,'admin-sub.html',{'adm':adm,'sub':sub})

def admin_one_sub(request,pk):
    adm = Admin.objects.get(email=request.session['email'])
    sub = Sub.objects.get(id=pk)
    if request.method == 'POST':
        sub.fname = request.POST['fname']
        sub.lname = request.POST['lname']
        sub.phone = request.POST['phone']
        if 'pic' in request.FILES:
            sub.pic = request.FILES['pic']
        
        sub.save()
    return render(request, 'admin-one-sub.html',{'adm':adm,'sub':sub})

def admin_feedback(request):
    adm = Admin.objects.get(email=request.session['email'])
    feed = Feedback.objects.all()
    return render(request,'admin-feedback.html',{'adm':adm,'feed':feed})

def admin_efeed(request,pk):
    adm = Admin.objects.get(email=request.session['email'])
    feed = Feedback.objects.get(id=pk)
    return render(request,'admin-efeedback.html',{'adm':adm,'feed':feed })


def admin_emegency(request):
    adm = Admin.objects.get(email=request.session['email'])
    return render(request,'admin-emergency.html',{'adm':adm})

def admin_rules(request):
    adm = Admin.objects.get(email=request.session['email'])
    return render(request,'admin-rules.html',{'adm':adm})

def admin_edit_profile(request):
    adm=Admin.objects.get(email=request.session['email'])
    if request.method == 'POST':
        adm.fname = request.POST['fname']
        adm.lname = request.POST['lname']
        
        if 'pic' in request.FILES:
            adm.pic = request.FILES['pic']
        adm.save()
    return render(request,'admin-edit-profile.html',{'adm':adm})

def admin_view_profile(request):
    adm=Admin.objects.get(email=request.session['email'])
    return render(request,'admin-view-profile.html',{'adm':adm})

def admin_password(request):
    adm=Admin.objects.get(email=request.session['email'])
    if request.method == 'POST':
        if request.POST['opassword'] == adm.password:
            if request.POST['password'] == request.POST['rpassword']:
                adm.password = request.POST['password']
                adm.save()
                return render(request,'admin-password.html',{'adm':adm,'msg':'Password has been changed'})
            return render(request,'admin-password.html',{'adm':adm,'msg':'New entered password are different'})
        return render(request,'admin-password.html',{'adm':adm,'msg':'Old Password is incorrect'})
    return render(request,'admin-password.html',{'adm':adm})

def category(request):
    adm=Admin.objects.get(email=request.session['email'])
    cate=Category.objects.all()
    return render(request,'category.html',{'adm':adm,'cate':cate })

from Inspector.models import MostWanted

def most_wanted_view(request):
    most_wanted_list = MostWanted.objects.all()
    return render(request, 'admin-mostw_view.html', {'most_wanted_list': most_wanted_list})

def most_wanted_one(request, pk):
    person = get_object_or_404(MostWanted, pk=pk)
    return render(request, 'admin-mostw_details.html', {'person': person})

def view_all_complaints(request):
    complaints = Complaint.objects.all()
    return render(request, 'admin-view-complaints.html', {'complaints': complaints})


#blog


from django.shortcuts import render, redirect
from .models import Admin, Post

from .models import Post, Comment
from django.shortcuts import redirect
from django.contrib import messages

def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')  # Assuming your form has a file input field with name 'image'
        
        if title and content:
            new_post = Post(title=title, content=content, published_date=timezone.now(), image=image)
            new_post.save()
            messages.success(request, 'Post added successfully!')
            return redirect('admin-index')  # Redirect to admin-index
        else:
            # Handle if any required fields are missing
            return render(request, 'add_post.html', {'error': 'Please fill in all required fields'})
    else:
        return render(request, 'add_post.html')
