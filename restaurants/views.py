from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "restaurants":Restaurant.objects.all()
    }
    return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
    context = {
        "restaurant": Restaurant.objects.get(id=restaurant_id)
    }
    return render(request, 'detail.html', context)

def restaurant_create(request):
    form = RestaurantForm()
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant-list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def restaurant_update(request, restaurant_id):
    my_obj = Restaurant.objects.get(id=restaurant_id)
    my_form = RestaurantForm(instance=my_obj)
    if request.method == "POST":
        my_form = RestaurantForm(request.POST, instance=my_obj)
        if my_form.is_valid():
            my_form.save()
            return redirect('restaurant-list')
    context = {
        "form": my_form,
        "restaurant":my_obj,
    }
    return render(request, 'update.html', context)

def restaurant_delete(request, restaurant_id):
    Restaurant.objects.get(id=restaurant_id).delete()
    return redirect('restaurant-list')


    return
