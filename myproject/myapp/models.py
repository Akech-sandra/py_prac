from django.db import models

# Create your models here.

class Details(models.Model):
    full_name =models.CharField( max_length= 200)
    email = models.EmailField( max_length=254)
    city = models.CharField( max_length= 200)
    phone_number = models.CharField( max_length= 200 )
    
    def __str__(self) -> str:
        return f'{self.city}'
    