from django.contrib import admin
from .models import Customer
# Register your models here.
@admin.register(Customer)
class CustumerAdminModel(admin.ModelAdmin):
    list_display=['id','name','email','created_at','phone','status']