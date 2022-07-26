from http.client import HTTPResponse
from django.shortcuts import redirect, render
from shop import form
from shop.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def home(request):
    return render(request, "shop/index.html")


def contact(request):
    if request.method == 'POST':
        form = Contact()
        query = request.POST
        name = query.get('name')
        email = query.get('email')
        message = query.get('message')

        form.name = name
        form.email = email
        form.message = message
        form.save()
        messages.success(request, "Data Added Sucessfully")
        return redirect('contact')
    return render(request, "shop/contact.html")


def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Sucess')
            return redirect('/login')
    return render(request, "shop/register.html", {'form': form})


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Sucessfully')
                return redirect("/")
            else:
                messages.error(request, "Invalid User Name or Password")
                return redirect("/login")
        return render(request, "shop/login.html")


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged Out Sucessfully")
        return redirect("/")


def collections(request):
    catagory = Catagory.objects.filter(status=0)
    return render(request, "shop/collections.html", {"catagory": catagory})


def collectionsview(request, name):
    if(Catagory.objects.filter(name=name, status=0)):
        products = Product.objects.filter(catagory__name=name)
        return render(request, "shop/products/index.html", {"products": products, "catagory": name})
    else:
        messages.warning(request, "No Such Catagory Found")
        return redirect('collections')


def vender(request):
    catagory = Catagory.objects.filter(status=0)
    if request.POST and request.FILES['propic']:
        form = Product()
        query = request.POST
        ownerName = query.get('ownername')
        petName = query.get('petname')
        ownerNumber = query.get('number')
        price = query.get('price')
        gender = query.get('gender')
        pic = request.FILES.get('propic')
        category = query.get('category')

        category_obj = Catagory.objects.get(name=category)
        form.owner_name = ownerName
        form.pet_name = petName
        form.owner_number = ownerNumber
        form.product_price = price
        form.gender = gender
        form.product_image = pic
        form.catagory = category_obj
        form.save()
        messages.success(request, "Data Added Sucessfully")
        return redirect('collections')

    return render(request, "shop/products/vendor_page.html", {"catagory": catagory})


def product_details(request, cname, pname):
    if(Catagory.objects.filter(name=cname, status=0)):
        if(Product.objects.filter(pet_name=pname, status=0)):
            products = Product.objects.filter(pet_name=pname, status=0).first()
            return render(request, "shop/products/product_details.html", {"products": products})
        else:
            messages.warning(request, "No Such Product Found")
            return redirect('collections')
    else:
        messages.warning(request, "No Such Catagory Found")
        return redirect('collections')


def profile(request):
    return render(request, "shop/profile/profile.html")
