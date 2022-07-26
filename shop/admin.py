from django.contrib import admin
from .models import *

# Register your models here.


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image')


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('catagory', 'owner_name', 'product_image')


admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Contact)
