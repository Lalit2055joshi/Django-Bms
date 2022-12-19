from django import forms
from .models import Customer,Subcription

class CustomerRegistration(forms.ModelForm):
    class Meta:
        model=Customer
        fields = '__all__'
        # fields=['name','created_at','email','phone','status']
        # widgets = {
        #     'name' : forms.TextInput(attrs={'class':'form-control'}),
        #     'email' : forms.EmailInput(attrs={'class':'form-control'}),
        #     'created_at':forms.DateField(attrs={'class':'form-control'}),
        #     'phone':forms.IntegerField(attrs={'class':'form-control'}),
        #     'status' : forms.ChoiceField(attrs={'class':'form-control'}),
        # }
class SubcriptionRegistration(forms.ModelForm):
    class Meta:
        model=Subcription
        fields = '__all__'
        
        