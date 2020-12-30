from django.shortcuts import render
from .models import *
from django.urls import reverse
from django.http import JsonResponse
import json
import datetime
from .utils import cookieCart,cartData,guestOrder
from django.core.mail import send_mail

def store(request):
    data=cartData(request)
    cartItems=data['cartItems']
    
        
    # categories=Category.objects.all()
    products=Product.objects.all()
    context={'products':products, 'cartItems':cartItems}
    return render(request,'store/store.html',context)
   

def category(request,title):
    categories=Category.objects.get(title=title)
    products=Product.objects.filter(title=categories)
    context={
        'categories':categories,
        'products':products,
    }
    return render(request,'categories.html',context)


def product(request):
    data=cartData(request)
    cartItems=data['cartItems']
    
    products=Product.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'store/products.html',context)

def abstract(request):
    data=cartData(request)
    cartItems=data['cartItems']
   
    
    products=Abstract.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'store/abstract.html',context)


def modern(request):
    data=cartData(request)
    cartItems=data['cartItems']
        
    products=Modern.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'store/modern.html',context)


def contemporary(request):
    data=cartData(request)
    cartItems=data['cartItems']
    
    products=Contemporary.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'store/contemporary.html',context)


def cubism(request):
    data=cartData(request)
    cartItems=data['cartItems']
    
    products=Cubism.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'store/cubism.html',context)

def surrealism(request):
    data=cartData(request)
    cartItems=data['cartItems']
    
    products=Surrealism.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'store/surrealism.html',context)


def impressionism(request):
    data=cartData(request)
    cartItems=data['cartItems']

    products=Impressionism.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'store/impressionism.html',context)




def cart(request):
    data=cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']
        
    context={ 'items':items,'order':order ,'cartItems':cartItems}
    return render(request,'store/cart.html',context)


def checkout(request):
        data=cartData(request)
        cartItems=data['cartItems']
        order=data['order']
        items=data['items']
    
        context={ 'items':items,'order':order,'cartItems':cartItems }
        return render(request,'store/checkout.html',context)

def updateItem(request):
    data=json.loads(request.body)
    productName=data['productName']
    action=data['action']

    print("Action: ",action)
    print("ProductName: ",productName)

    customer=request.user.customer
    product=Product.objects.get(name=productName)
    # product=Abstract.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)
    

    if action == 'add':
        orderItem.quantity= (orderItem.quantity + 1 )
    elif action == 'remove':
        orderItem.quantity=(orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity==0:
        orderItem.delete()
            #orderItem.quantity==0
    
    

    # if orderItem.quantity <= 0:
    #     orderItem.delete()
    return JsonResponse('Item was added', safe =False)

def updateab(request):
    data=json.loads(request.body)
    productName=data['productName']
    action=data['action']

    print("Action: ",action)
    print("productName: ",productName)

    customer=request.user.customer
    product=Product.objects.get(name=productName)
    order,created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)
    
    if action == 'add':
        orderItem.quantity= (orderItem.quantity + 1 )
    elif action == 'remove':
        orderItem.quantity=(orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()

    # if action == 'add':
    #     orderItem.quantity= (orderItem.quantity + 1)
    # elif action == 'remove':
    #     orderItem.quantity=(orderItem.quantity - 1)
    
    # orderItem.save()

    # if orderItem.quantity <= 0:
    #     orderItem.delete()
    return JsonResponse('Item was added', safe =False)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def processOrder(request):
    transaction_id =datetime.datetime.now().timestamp()
    data= json.loads(request.body)

    if request.user.is_authenticated:
        customer=request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        # total=float(data['form']['total'])
        # order.transaction_id=transaction_id

    else:
        customer, order = guestOrder(request,data)


    total=float(data['form']['total'])
    order.transaction_id=transaction_id

    if total == order.get_cart_total:
         order.complete=True
    order.save()
    if order.shipping == True:
        ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
                
  
            )
    return JsonResponse('Payment Complete',safe=False)
# Create your views here.
