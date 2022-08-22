from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import *

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/Store.html',context)

def cart(request):

    if request.user:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {'items': items, 'order': order}
    return render(request, 'store/Cart.html', context)

def checkout(request):
    if request.user:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {'items': items, 'order': order}
    return render(request, 'store/Checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action',action)
    print('productId',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer = customer,complete = False)

    orderItem,created = orderItem.objects.get_or_create(order = order,product = product)

