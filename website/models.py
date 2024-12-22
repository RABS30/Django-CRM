from ctypes import addressof
from django.db import models

class Records(models.Model):
    created     = models.DateField(auto_now_add=True)
    firstName   = models.CharField(("Nama Depan"), max_length=50)
    lastName    = models.CharField(("Nama Belakang"), max_length=50)
    address     = models.CharField(("Email"), max_length=50)
    city        = models.CharField(("Kota"), max_length=50)
    state       = models.CharField(("Provinsi"), max_length=50)
    zipcode     = models.CharField(("Kode Pos"), max_length=20)
    phone       = models.CharField(("Telepon"), max_length=15)
    
    
    
    def __str__(self) :
        return self.firstName + ' ' + self.lastName