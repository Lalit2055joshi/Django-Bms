from django.db import models
from django.core.exceptions import ValidationError
def validate_amount(value):
    if value < 0:
        raise ValidationError(
            ('%(value)s enter amount is negative'),
            params={'value': value},
        )


ACTIVE = 'active'
INACTIVE = 'inactive'
state=(
    (ACTIVE,ACTIVE),
    (INACTIVE,INACTIVE)
    )
class Customer(models.Model):
    name = models.CharField(max_length=50,unique=True)
    created_at = models.DateField(auto_now=True)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()
    status=models.CharField(max_length=10,choices=state)
    
    def __str__(self):
        return self.name

PAID = 'paid'
UNPAID = 'unpaid'
payment_choice=(
    (PAID,PAID),
    (UNPAID,UNPAID))
class Subcription(models.Model):  
    customer_name = models.CharField(max_length=50)
    from_date = models.DateField(auto_now=True)
    to_date = models.DateField()
    amount=models.FloatField(validators=[validate_amount])
    status= models.CharField(max_length=40,choices=payment_choice)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name
