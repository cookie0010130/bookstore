from django.shortcuts import render, redirect
from order.models import Product
from order.forms import ProductForm

def order(request):
    template = 'order/order.html'
    if request.method == 'GET':
        return render(request, template, {'productForm':ProductForm()})

    # POST
    productForm = ProductForm(request.POST)
    if not productForm.is_valid():
        return render(request, template, {'productForm':productForm})

    productForm.save()
    return redirect('order:ordercheck')

def ordercheck(request):
    products = Product.objects.all().order_by('-id')[:1] 
    context = {'products':products}
    return render(request,'order/ordercheck.html',context)

