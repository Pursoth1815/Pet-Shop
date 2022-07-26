# Create your Backend Tables here


def getFileName(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"(now_time, filename)
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
    owner_number = models.IntegerField(null=False, blank=False)
    product_price = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name


************* Command ***********

// python manage.py makemigration 

incase of error it shows 

// python manage.py migrate

after migrate tables will created

// python manage.py createsuperuser

it will ask name, email , pass { it willl not display  }


STEPS TO FOLLLOW

Theme installation - pip install django-jazzmin

and add it on installed APPS tooo

