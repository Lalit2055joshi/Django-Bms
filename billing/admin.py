from django.contrib import admin
from .models import Customer,Subcription
# Register your models here.
@admin.register(Customer)
class CustumerAdminModel(admin.ModelAdmin):
    list_display=['id','name','email','created_at','phone','status']

@admin.register(Subcription)
class SubscriberAdminModel(admin.ModelAdmin):
    list_display=['id','customer_name','from_date','to_date','amount','status','customer']
