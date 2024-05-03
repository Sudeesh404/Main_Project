from ast import Pass
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import randrange
# Create your views here.


# Front Page
def index(request):
    return render(request,'index.html')


# Register Block

def register(request):
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            msg = 'Email already exists'
            return render(request,'register.html',{'msg':msg})
        except:
            if request.POST['password'] == request.POST['rpassword']:
                otp = randrange(10000,99999) 
                print(otp)  
                subject = 'ONE TIME PASSWORD FOR USER REGISTRATION'
                message = f'{otp} please paste this number in the OTP field to verify your account.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                global data 
                data = {
                    'fname' : request.POST['fname'],
                    'lname' : request.POST['lname'],
                    'email' : request.POST['email'],
                    'phone' : request.POST['phone'],
                    'password' : request.POST['password'],
                }

                
                return render(request,'otp.html',{'msg':'OTP sent', 'otp':otp})
            return render(request,'register.html',{'msg':'Both password are not same'})
    return render(request,'register.html')




def otp(request):
    if request.method == 'POST':
        if request.POST['otp']  == request.POST['uotp']:
            global data
            User.objects.create(
                fname = data['fname'],
                lname = data['lname'],
                email = data['email'],
                phone = data['phone'],
                password = data['password'],
            )
            return render(request,'citizen.html',{'msg':'Account Created'})
        return render(request,'otp.html',{'msg':'Invalid OTP', 'otp' : request.POST['otp']})
    return render(request,'citizen.html')

# Login Block

def citizen(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.POST['email'])
            if request.POST['password'] == uid.password:
                request.session['email'] = request.POST['email']
                return redirect('home')
            return render(request,'citizen.html',{'msg':'Incorrect Password'})
        except:
            msg = 'E-mail not registered' 
            return render(request,'citizen.html',{'msg':msg})
    return render(request,'citizen.html')


# Citizen Block
def home(request):
    uid = User.objects.get(email=request.session['email']) 
    return render(request,'home.html',{'uid':uid})

def add_FIR(request):
    uid = User.objects.get(email=request.session['email'])
    stationary = Station.objects.all()
    if request.method == 'POST':
        stat = Station.objects.get(id=request.POST['police'])
        if 'evi' and 'ID' in request.FILES:
            FIR.objects.create(
                applicant=uid,
                date=request.POST['date'],
                idate=request.POST['rdate'],
                time=request.POST['time'],
                address=request.POST['address'],
                landmark=request.POST['landmark'],
                charge=request.POST['charge'],
                victim=request.POST['victim'],
                ifname=request.POST['fname'],
                ilname=request.POST['lname'],
                dob=request.POST['dob'],
                iaddress=request.POST['info_address'],
                sfname=request.POST['sname'],
                slname=request.POST['slname'],
                sdetail=request.POST['sdetail'],
                evi=request.FILES['evi'],
                iid=request.FILES['ID'],
                police=stat
            )
        else:
            FIR.objects.create(
                applicant=uid,
                date=request.POST['date'],
                idate=request.POST['rdate'],
                time=request.POST['time'],
                address=request.POST['address'],
                landmark=request.POST['landmark'],
                charge=request.POST['charge'],
                victim=request.POST['victim'],
                ifname=request.POST['fname'],
                ilname=request.POST['lname'],
                dob=request.POST['dob'],
                iaddress=request.POST['info_address'],
                sfname=request.POST['sname'],
                slname=request.POST['slname'],
                sdetail=request.POST['sdetail'],
                police=stat
                )
        msg = 'FIR Added'
        return render(request,'add_FIR.html',{'uid':uid,'stationary':stationary,'msg':msg})
    return render(request,'add_FIR.html',{'uid':uid,'stationary':stationary})

def view_FIR(request):
    uid = User.objects.get(email=request.session['email'])
    FIRs= FIR.objects.filter(applicant=uid)
    return render(request,'view-FIR.html',{'uid':uid,'FIRs':FIRs})

def view_one_FIR(request,pk):
    uid = User.objects.get(email=request.session['email'])
    fir=FIR.objects.get(id=pk)
    return render(request, 'view-one-FIR.html',{'uid':uid,'fir':fir})

def search_station(request):
    uid = User.objects.get(email=request.session['email'])
    stations= Station.objects.all()
    return render(request, 'search_station.html',{'uid':uid,'stations':stations})

def add_com(request):
    uid = User.objects.get(email=request.session['email'])
    ins_queryset = Ins.objects.all()  # Fetching all instances of Ins
    if request.method == 'POST':
        selected_ins = Ins.objects.get(id=request.POST['police'])  # Fetch the selected Ins instance
        Complaint.objects.create(
            applicant=uid,
            date=request.POST['date'],
            idate=request.POST['rdate'],
            time=request.POST['time'],
            address=request.POST['address'],
            landmark=request.POST['landmark'],
            charge=request.POST['charge'],
            victim=request.POST['victim'],
            ifname=request.POST['fname'],
            ilname=request.POST['lname'],
            dob=request.POST['dob'],
            iaddress=request.POST['info_address'],
            police=selected_ins  # Assign the selected Ins instance to the police field
        )
        msg = 'Complaint Added'
        return render(request, 'home.html', {'uid': uid, 'ins_queryset': ins_queryset, 'msg': msg})
    
    return render(request, 'add_com.html', {'uid': uid, 'ins_queryset': ins_queryset})


def view_com(request):
    uid = User.objects.get(email=request.session['email'])
    com= Complaint.objects.filter(applicant=uid)
    return render(request,'view-com.html',{'uid':uid,'com':com})

def view_one_com(request,pk):
    uid = User.objects.get(email=request.session['email'])
    com=Complaint.objects.get(id=pk)
    return render(request, 'view-one-com.html',{'uid':uid,'com':com})

def feedback(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        Feedback.objects.create(
            applicant=uid,
            title=request.POST['title'],
            feed=request.POST['feed']
            

        )
        msg='Feedback Sent'
        return render(request,'feedback.html',{'uid':uid, 'msg':msg })
    return render(request,'feedback.html',{'uid':uid})
    




# Header Block

def edit_profile(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.fname = request.POST['fname']
        uid.lname = request.POST['lname']
        uid.phone = request.POST['phone']
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        uid.save()
    return render(request,'eprofile.html',{'uid':uid})

def view_profile(request):
    uid=User.objects.get(email=request.session['email'])
    return render(request,'view-profile.html',{'uid':uid})

def password(request):
    uid = User.objects.get(email = request.session['email'])
    if request.method == 'POST':
        if request.POST['opassword'] == uid.password:
            if request.POST['password'] == request.POST['rpassword']:
                uid.password = request.POST['password']
                uid.save()
                return render(request,'password.html',{'uid':uid,'msg':'Password has been changed'})
            return render(request,'password.html',{'uid':uid,'msg':'New entered password are different'})
        return render(request,'password.html',{'uid':uid,'msg':'Old Password is incorrect'})
    return render(request,'password.html',{'uid':uid})


def logout(request): 
    del request.session['email']
    return redirect('index')

# Emergency 

def emergency(request):
    return render(request,'emergency.html')

def rules(request):
    return render(request,'rules.html')

def missing(request):
    miss=Missing.objects.all()
    return render(request,'missing.html',{'miss':miss})

def missing_one(request,pk):
    miss=Missing.objects.get(id=pk)
    return render(request, 'missing-one.html',{'miss':miss})

from django.shortcuts import render, redirect
from .models import Missing

def add_missing(request):
    stationary = Missing.objects.all()  # Assuming you want to list all missing persons
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('address')
        area = request.POST.get('area')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        contact = request.POST.get('contact')
        status = request.POST.get('status')
        pic = request.FILES.get('pic', 'default.jpg')  # 'default.jpg' should be your default image path

        Missing.objects.create(
            fname=fname,
            lname=lname,
            address=address,
            area=area,
            height=height,
            weight=weight,
            contact=contact,
            status=status,
            pic=pic
        )
        return redirect('success_view')  # Redirect to a success page or any other URL

    return render(request, 'add_missing.html', {'stationary': stationary})

def success_view(request):
    return render(request, 'home.html')

from Inspector.models import MostWanted

def most_wanted(request):
    most_wanted_list = MostWanted.objects.all()
    return render(request, 'mostwanted.html', {'most_wanted_list': most_wanted_list})

def one_most_wanted(request, pk):
    person = get_object_or_404(MostWanted, pk=pk)
    return render(request, 'one-mostwanted.html', {'person': person})

#complaintprint
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from .models import Complaint

def generate_pdf(request, complaint_id):
    try:
        # Fetch complaint details from the database
        complaint = Complaint.objects.get(id=complaint_id)

        # Create a PDF document
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'filename="complaint_{complaint.id}.pdf"'
        doc = SimpleDocTemplate(response, pagesize=letter)
        # Define styles for text
        styles = getSampleStyleSheet()
        title_style = styles['Title']
        paragraph_style = styles['BodyText']
        
        paragraph_style = ParagraphStyle(name='Justify', alignment=4)
        # Create content for the PDF
        
        elements = []
       
        elements.append(Spacer(1, 12))
        logo_path = 'D:\MainProject\myapp\static\images\Kerala_State_Police_Logo.png'  # Replace this with the path to your logo file
        logo = Image(logo_path, width=100, height=100)
        elements.append(logo)
        elements.append(Paragraph("Complaint Details", title_style))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"Complaint ID: {complaint.id}", paragraph_style))
        elements.append(Paragraph(f"Applicant: {complaint.applicant.fname} {complaint.applicant.lname}", paragraph_style))
        elements.append(Paragraph(f"Police Station: {complaint.police.station_name}", paragraph_style))
        elements.append(Paragraph(f"Date: {complaint.date}", paragraph_style))
        elements.append(Paragraph(f"Time: {complaint.time}", paragraph_style))
        elements.append(Paragraph(f"Address: {complaint.address}", paragraph_style))
        elements.append(Paragraph(f"Landmark: {complaint.landmark}", paragraph_style))
        elements.append(Paragraph(f"Charge: {complaint.charge}", paragraph_style))
        elements.append(Paragraph(f"Victim: {complaint.victim}", paragraph_style))
        elements.append(Paragraph(f"Informant: {complaint.ifname} {complaint.ilname}", paragraph_style))
        elements.append(Paragraph(f"Date of Birth: {complaint.dob}", paragraph_style))
        elements.append(Paragraph(f"Informant Address: {complaint.iaddress}", paragraph_style))
        elements.append(Paragraph(f"Status: {'Approved' if complaint.status else 'Not Approved'}", paragraph_style))
        elements.append(Spacer(1, 12))
        justified_paragraph = Paragraph(
            "We would like to inform you that your complaint has been successfully registered with us. "
            "Our team is diligently reviewing the details provided, and we assure you that appropriate actions will be taken. "
            "Your cooperation in this matter is greatly appreciated. "
            "We understand the importance of your concern, and we assure you that our authorities will reach out to you shortly to address the issue further.",
            paragraph_style
        )
        elements.append(justified_paragraph)
        elements.append(Spacer(1, 12))

        elements.append(Paragraph(f"Thank you for bringing this matter to our attention."))
        elements.append(Spacer(1, 12))

        elements.append(Paragraph(f"Sincerely,"))
        elements.append(Spacer(1, 12))

        elements.append(Paragraph(f"Kottayam Police"))
                         

        
        # Build the PDF document
        doc.build(elements)

        return response
    except Exception as e:
        # Handle exceptions gracefully
        return HttpResponse(f"Error: {e}")
    
    #blog
from Admin.models import Post, Comment
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog_post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            comment = Comment.objects.create(post=post, text=text)
            return redirect('post_detail', pk=pk)
    return render(request, 'blogpost_detail.html', {'post': post})

