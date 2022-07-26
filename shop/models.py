from django.db import models
import datetime
import os
from django.contrib.auth.models import User

# Create your models here.


def getFileName(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s" % (now_time, filename)
    return os.path.join('uploads/', new_filename)


class Catagory(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    status = models.BooleanField(default=False, help_text="0-Show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=150, null=False, blank=False)
    pet_name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(
        upload_to=getFileName, null=True, blank=True)
    owner_number = models.BigIntegerField(null=False, blank=False, unique=True)
    product_price = models.FloatField(null=False, blank=False)
    gender = models.CharField(
        max_length=10, null=True, blank=False)
    status = models.BooleanField(default=0, help_text="0-Show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pet_name


class Contact(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(
        max_length=150, null=False, blank=False, unique=True)
    message = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.email
