from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100)
    problem=models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name_plural="Contact Us"