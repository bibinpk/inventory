from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(request):
    move_details = movements.objects.all().order_by('time').reverse()
    return render(request,'index.html',{'moves':move_details})

def addproduct(request):
    if request.method == 'POST':
        product = request.POST['product']
        obj = products.objects.create(product_name=product)
        obj.save()
        return redirect('/products/')
    else:
        pro_details = products.objects.all()
        return render(request,'products.html',{'products':pro_details})

def editproduct(request,product_id):
    if request.method == 'POST':
        id = request.POST['id']
        pro = request.POST['product']
        obj = products.objects.filter(id=id).update(product_name=pro)
        return redirect('/')
    else:
        pro = products.objects.get(id=product_id)
        return render(request,'product.html',{'product':pro})

def deleteproduct(request,product_id):
    obj=products.objects.get(id=product_id)
    obj.delete()
    return redirect('/')

def addlocation(request):
    if request.method == 'POST':
        location = request.POST['location']
        obj = locations.objects.create(location_name=location)
        obj.save()
        return redirect('/locations/')
    else:
        loc_details = locations.objects.all()
        return render(request,'locations.html',{'locations':loc_details})

def editlocation(request,location_id):
    if request.method == 'POST':
        id = request.POST['id']
        loc = request.POST['location']
        obj = locations.objects.filter(id=id).update(location_name=loc)
        return redirect('/')
    else:
        loc = locations.objects.get(id=location_id)
        return render(request,'location.html',{'location':loc})

def deletelocation(request,location_id):
    obj=locations.objects.get(id=location_id)
    obj.delete()
    return redirect('/')

def addmovement(request):
    if request.method == 'POST':
        product=request.POST['product']
        quantity=request.POST['quantity']
        location_from=request.POST['location_from']
        location_to=request.POST['location_to']
        pro=products.objects.get(product_name=product)
        loc1=locations.objects.get(location_name=location_from)
        loc2=locations.objects.get(location_name=location_to)
        obj=movements.objects.create(product=pro,location_from=loc1,location_to=loc2,quantity=quantity)
        obj.save()
        return redirect('/')
    else:
        prod = products.objects.all()
        loc = locations.objects.all()
        move_details = movements.objects.all()
        return render(request,'movements.html',{'movements':move_details,'locations':loc,'products':prod})

def editmovement(request,movement_id):
    if request.method == 'POST':
        id = request.POST['id']
        product=request.POST['product']
        quantity=request.POST['quantity']
        location_from=request.POST['location_from']
        location_to=request.POST['location_to']
        pro=products.objects.get(product_name=product)
        loc1=locations.objects.get(location_name=location_from)
        loc2=locations.objects.get(location_name=location_to)
        obj=movements.objects.filter(id=id).update(product=pro,location_from=loc1,location_to=loc2,quantity=quantity)
        return redirect('/')
    else:
        move = movements.objects.get(id=movement_id)
        pro = products.objects.all()
        loc = locations.objects.all()
        return render(request,'movement.html',{'movement':move,'products':pro,'locations':loc})

def deletemovement(request,movement_id):
    obj=movements.objects.get(id=movement_id)
    obj.delete()
    return redirect('/')