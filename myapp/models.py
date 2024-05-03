from django.db import models
from Inspector.models import Ins


# Create your models here.
class User(models.Model):
    fname= models.CharField(max_length=40)
    lname= models.CharField(max_length=40)
    email= models.EmailField(unique=True)
    phone= models.CharField(max_length=40)
    password=models.CharField(max_length=10)
    pic= models.FileField(upload_to = 'Profile', default='default.jpg')


    def __str__(self) :
	    return self.fname + ' ' + self.lname

class Station(models.Model):

    station = models.CharField(max_length=50)
    img = models.FileField(upload_to='Station', default='police station.jpg')
    address= models.TextField(null=True, blank=True)

    def __str__(self):
        return self.station

class FIR(models.Model):
    
    applicant= models.ForeignKey(User,on_delete=models.CASCADE)
    police= models.ForeignKey(Ins,on_delete=models.CASCADE)
    date= models.CharField(max_length=50,null=True,blank=True)
    idate= models.CharField(max_length=50)
    time= models.CharField(max_length=6)
    address= models.CharField(max_length=100)
    landmark= models.CharField(max_length=50)
    charge = models.CharField(max_length=100)
    victim = models.CharField(max_length=10, null=True,blank=True)
    ifname= models.CharField(max_length=50)
    ilname= models.CharField(max_length=50)
    dob= models.CharField(max_length=50)
    iid= models.FileField(upload_to ='Informant ID', null=True,blank=True)
    iaddress= models.CharField(max_length=100)
    evi=models.FileField(upload_to='Evidence', null = True,blank=True)
    sfname=models.CharField(max_length=50, null=True,blank=True)
    slname=models.CharField(max_length=50, null=True,blank=True)
    sdetail=models.TextField(null=True,blank=True)
    status=models.BooleanField(default=False)


    def __str__(self):
        return self.applicant.fname + ' >> ' + self.idate
    

class Complaint(models.Model):
    applicant= models.ForeignKey(User,on_delete=models.CASCADE)
    police= models.ForeignKey(Ins,on_delete=models.CASCADE)
    date= models.DateField(null=True)
    idate= models.DateField(null=True)
    time= models.CharField(max_length=6)
    address= models.CharField(max_length=100)
    landmark= models.CharField(max_length=50)
    charge = models.CharField(max_length=100)
    victim = models.CharField(max_length=10, null=True,blank=True)
    ifname= models.CharField(max_length=50)
    ilname= models.CharField(max_length=50)
    dob= models.DateField(null=True)
    iaddress= models.CharField(max_length=100)
    status=models.BooleanField(default=False)
 

    def __str__(self):
        return self.applicant.fname + '  ' + self.applicant.lname

class Feedback(models.Model):
    applicant= models.ForeignKey(User,on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    feed=models.TextField()
    

    def __str__(self):
        return self.applicant.fname + ' ' + self.applicant.lname

class Missing(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    area=models.CharField(max_length=50)
    height=models.CharField(max_length=10)
    weight=models.CharField(max_length=10)
    contact=models.CharField(max_length=10)
    status=models.BooleanField(default=False)
    pic=models.FileField(null = True, blank=True, default='default.jpg')


    def __str__(self):
        return self.fname + ' ' + self.lname
