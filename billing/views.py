from django.shortcuts import render,HttpResponseRedirect
from .models import *
from .forms import *
from email.message import EmailMessage
# from BMS import password
import ssl
import smtplib

def add_show(request):
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
    cust = Customer.objects.all() 
    return render(request,'billing/addandshow.html',{'form':fm,'cus':cust})

def update_data(request,id):
    pi = Customer.objects.get(pk=id)
    fm = CustomerRegistration(request.POST,instance=pi)
    if request.method == 'POST':
        pi = Customer.objects.get(pk=id)
        fm = CustomerRegistration(request.POST,instance=pi)
        fm.save()
        if fm.is_valid():
            fm.save()     
        else:
            pi = Customer.objects.get(pk=id)
            fm = CustomerRegistration(instance=pi)    
    return render(request,"billing/updatecustomer.html", {"form":fm})


#THis function will Delete 
def delete_data(request,id):
    if request.method == "POST":
        pi = Customer.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def getactivecustomer(request):
    activecustomer=Customer.objects.filter(status=ACTIVE)
    return render(request,"billing/activecustomer.html",{"ac":activecustomer})

def getinactivecustomer(request):
    inactivecustomer=Customer.objects.filter(status=INACTIVE)
    return render(request,"billing/inactivecustomer.html",{'ia':inactivecustomer})



# def sendemail(request):
#     email_sender='074bex006.lalit@sagarmatha.edu.np'
#     email_password='yybjkbusiqtabkqo'
#     email_receiver=row['email']

#     subject="Subscription time is going to timeout!!!"
#     body=""""
#             Your subscripton is running out so please buy subscription at timely.
#             Thank You!!!


#             """      
#     em=EmailMessage()
#     em['from']=email_sender
#     em['to']=email_receiver
#     em['subject']=subject
#     em.set_content(body)
#     context=ssl.create_default_context()
#     with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
#         smtp.login(email_sender,email_password)
#         smtp.sendmail(email_sender,email_receiver,em.as_string())


# def add_show_customer(request):
#     if request.method=='POST':
#         fm = SubcriptionRegistration(request.POST)
#         if fm.is_valid():
#             nm = fm.cleaned_data['customer_name']
#             fd = fm.cleaned_data['from_date']
#             td=fm.cleaned_data['to_date']
#             amt=fm.cleaned_data['amount']
#             stat=fm.cleaned_data['status']
#             cust=fm.cleaned_data['customer']
#             reg = Customer(name=nm,from_date=fd,to_date=td,amount=amt,status=stat,customer=cust)
#             reg.save()
#             fm = CustomerRegistration(request.POST)
#     else:
#         fm=SubcriptionRegistration()   
#     sub = Subcription.objects.all() 
#     return render(request,'billing/addandshowsubscriber.html',{'form':fm,'sub':sub})

# def update_data(request,id):
#     pi = Subcription.objects.get(pk=id)
#     fm = SubcriptionRegistration(request.POST,instance=pi)
#     if request.method == 'POST':
#         pi = Subcription.objects.get(pk=id)
#         fm = SubcriptionRegistration(request.POST,instance=pi)
#         fm.save()
#         if fm.is_valid():
#             fm.save()     
#         else:
#             pi = Subcription.objects.get(pk=id)
#             fm = SubcriptionRegistration(instance=pi)    
#     return render(request,"billing/updatecustomer.html", {"form":fm})


# #THis function will Delete 
# def delete_data(request,id):
#     if request.method == "POST":
#         pi = Subcription.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')


# def getpaidcustomer(request):
#     activecustomer=Subcription.objects.filter(status=ACTIVE)
#     return render(request,"billing/activecustomer.html",{"ac":activecustomer})

# def getunpaidcustomer(request):
#     inactivecustomer=Subcription.objects.filter(status=INACTIVE)
#     return render(request,"billing/inactivecustomer.html",{'ia':inactivecustomer})
