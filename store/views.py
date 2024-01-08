from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Order, Product
from django.views.generic import ListView
# Create your views here.

class ProductsPageView(ListView):
    template_name='store/store.html'
    model=Product
    context_object_name='products'
    
    def get_queryset(self):
        return super().get_queryset()

 
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
    context={'items':items,'order':order}
    return render(request,'store/cart.html',context)
        
        
def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
    
    context={'items':items,'order':order}
    return render(request,'store/checkout.html',context)