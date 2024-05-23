from django.db import models

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=100)
    school_name=models.CharField(max_length=200)
    
    
    
def __str__(self):
    return self.name
