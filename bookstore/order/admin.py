from django.contrib import admin
from order.models import Product

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','amount','name','number']

admin.site.register(Product,ProductModelAdmin)