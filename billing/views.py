from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import *
from .forms import CustomerRegistration,SubcriptionRegistration
from email.message import EmailMessage
from django.contrib.auth.models import Group
# from BMS import password
import ssl
import smtplib
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# @login_required(login_url='signin')
def add_show(request):   
    cust = Customer.objects.all() 
    return render(request,'billing/addandshow.html',{'cus':cust})


def add_customer(request):
    if request.user.groups.filter(permissions__name='Can add customer'):
        if request.method=='POST':
            fm = CustomerRegistration(request.POST)
            if fm.is_valid():
                nm = fm.cleaned_data['name']
                em = fm.cleaned_data['email']
                stat=fm.cleaned_data['status']
                phon=fm.cleaned_data['phone']
                reg = Customer(name=nm,email=em,status=stat,phone=phon)
                reg.save()
                fm = CustomerRegistration(request.POST)
        else:
            fm=CustomerRegistration()   
    else:
        messages.success(request,"Unauthorized")
        return redirect('/') 
    return render(request,'billing/createcustomer.html',{'form':fm})


def update_data(request,id):
    # import pdb;pdb.set_trace()
    if request.user.groups.filter(permissions__name='Can change customer'):
        if request.method == 'POST':
            pi = Customer.objects.get(pk=id)
            fm = CustomerRegistration(request.POST,instance=pi)
            fm.save()
            if fm.is_valid():
                fm.save()     
        else:
            pi = Customer.objects.get(pk=id)
            fm = CustomerRegistration(instance=pi) 
    else:
        messages.success(request,"you are not authorized")
        return redirect('/')         
    return render(request,"billing/updatecustomer.html", {"form":fm})


#THis function will Delete 
def delete_data(request,id):
    if request.user.groups.filter(permissions__name='Can change customer'):
        if request.method == "POST":
            pi = Customer.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/')
    else:
        messages.success(request,"you are not authorized")
        return redirect('/')

def getactivecustomer(request):
    activecustomer=Customer.objects.filter(status=ACTIVE)
    return render(request,"billing/activecustomer.html",{"ac":activecustomer})

def getinactivecustomer(request):
    inactivecustomer=Customer.objects.filter(status=INACTIVE)
    return render(request,"billing/inactivecustomer.html",{'ia':inactivecustomer})



def sendemail(request):
    from datetime import datetime,timedelta
    email_sender='074bex006.lalit@sagarmatha.edu.np'
    email_password='yybjkbusiqtabkqo'
    # email_receiver=row['email']
    subs=Subcription.objects.all()
    for i in subs:
        start_date=i.from_date
        to_date = i.to_date
        differ=to_date-start_date
        print(differ)
        print(i.status)
        x=timedelta(days=5)
        
        if differ <= x and i.status == 'paid':
            email_receiver = i.customer.email
    

    subject="Subscription time is going to timeout!!!"
    body=""""
            Your subscripton is running out so please buy subscription at timely.
            Thank You!!!


            """      
    em=EmailMessage()
    em['from']=email_sender
    em['to']=email_receiver
    em['subject']=subject
    em.set_content(body)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
    return render(request,'billing/Emailmessage.html')

@login_required(login_url='addandshow')
def add_show_customer(request):
    if request.user.groups.filter(permissions__name='Can change subcription'):
        if request.method=='POST':
            fom = SubcriptionRegistration(request.POST)
            if fom.is_valid():
                nm = fom.cleaned_data['customer_name']
                td=fom.cleaned_data['to_date']
                amt=fom.cleaned_data['amount']
                stat=fom.cleaned_data['status']
                cust=fom.cleaned_data['customer']
                reg = Subcription(customer_name=nm,to_date=td,amount=amt,status=stat,customer=cust)
                reg.save()
                fom = SubcriptionRegistration(request.POST)
        else:
            fom=SubcriptionRegistration()   
        sub = Subcription.objects.all()
    else:
        return redirect('/') 
    return render(request,'billing/addandshowsubscriber.html',{'form':fom,'sub':sub})



def update_customer_data(request,id):
    if request.user.groups.filter(permissions__name='can change subcription'):
        pi = Subcription.objects.get(pk=id)
        fm = SubcriptionRegistration(request.POST,instance=pi)
        if request.method == 'POST':
            pi = Subcription.objects.get(pk=id)
            fm = SubcriptionRegistration(request.POST,instance=pi)
            fm.save()
            if fm.is_valid():
                fm.save()     
            else:
                pi = Subcription.objects.get(pk=id)
                fm = SubcriptionRegistration(instance=pi) 
    else:
        return redirect('/')   
    return render(request,"billing/updatesubscriber.html", {"form":fm})


# #THis function will Delete 
def delete_customer_data(request,id):
    if request.user.groups.filter(permissions__name='can delete subcription'):
        if request.method == "POST":
            de = Subcription.objects.get(pk=id)
            de.delete()
    return redirect('addandshowcustomer')


def getpaidsubscriber(request):
    paidsubscriber=Subcription.objects.filter(status=PAID)
    return render(request,"billing/paidsubscriber.html",{"pd":paidsubscriber})

def getunpaidsubscriber(request):
    unpaidsubscriber=Subcription.objects.filter(status=UNPAID)
    return render(request,"billing/unpaidsubscriber.html",{'up':unpaidsubscriber})

def get_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "billing/signup.html", {"form": form})


def get_signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "billing/signin.html", {"form": form})

def logoutpage(request):
    logout(request)
    return redirect("addandshow")