from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.ProductsPageView.as_view(),name='home'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout')
]
