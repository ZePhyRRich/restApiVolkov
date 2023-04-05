from asyncio import transports
from multiprocessing import context
from unicodedata import category, decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
import random
from django.conf import settings
from rest_framework import generics
from .serializers import *
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
def home(request):
    retrive_type = models.RetriveType.objects.all()

    context = {
        'retrive_type':retrive_type
    }
    return render(request, 'mainSite/home.html', context)


def route(request):
    print('gedsa')
    if request.method == 'POST':
        order_route = models.OrderRoute.objects.filter(order = request.POST.get('route'))
        print(order_route)
        context = {
            'order_route':order_route
        }
        return render(request, 'mainSite/profile/route.html', context)
    
    return render(request, 'mainSite/profile/route.html')

@login_required
def my_order(request):

    
    if request.user.is_superuser:
            return redirect('../admin/')

    order = models.Order.objects.filter(user = request.user).order_by('-id')
    # response = requests.get('http://127.0.0.1:8000/api/v1/orders/')
    # order = response.json()
    context = {
        'order':order
    }

    return render(request, 'mainSite/profile/my_order.html', context)

@login_required
def order_route(request, pk):
    order_route = models.OrderRoute.objects.filter(order = pk)
    # response = requests.get('http://127.0.0.1:8000/api/v1/orders/')
    # order = response.json()
    print(order_route)
    context = {
        'order_route':order_route
    }

    return render(request, 'mainSite/profile/order_route.html', context)



@login_required
def make_order(request):
    city = models.City.objects.all()
    type = models.RetriveType.objects.all()
    city_list = models.City.objects.all()

    if request.POST:
        user = request.user.id,
        name = request.POST.get('name'),
        second_name = request.POST.get('second_name'),
        patronymic = request.POST.get('patronymic'),
        retrive_type =request.POST.get('retrive_type'),
        delivery_name = request.POST.get('delivery_name'),
        weight = request.POST.get('weight'),
        from_city = request.POST.get('from_city'),
        to_city = request.POST.get('to_city'),
        status = request.POST.get('status'),

        response_type = requests.post('http://127.0.0.1:8000/api/v1/create_order/', data={
            'user': user,
            'name': name,
            'second_name': second_name,
            'patronymic': patronymic,
            'retrive_type': retrive_type,
            'delivery_name': delivery_name,
            'weight': weight,
            'from_city': from_city,
            'to_city': to_city,
            'status': status,
    
        })
        # return redirect('home')

    # if request.method == 'POST':
    #     order = models.Order.objects.create(
    #         user = request.user,
    #         name = request.POST.get('name'),
    #         second_name = request.POST.get('second_name'),
    #         patronymic = request.POST.get('patronymic'),
    #         retrive_type = models.RetriveType.objects.get(pk=request.POST.get('retrive_type')),
    #         delivery_name = request.POST.get('delivery_name'),
    #         weight = request.POST.get('weight'),
    #         from_city = models.City.objects.get(pk=request.POST.get('from_city')),
    #         to_city = models.City.objects.get(pk=request.POST.get('to_city')),
    #         status = models.Status.objects.get(pk=7),
    #         )

        transport = models.Transport.objects.all().filter(retrive_type=request.POST.get('retrive_type')),

        random_city = random.choice(city_list)
    
        order = models.Order.objects.filter(user = request.user.id).last()
        models.OrderRoute.objects.create(
            order = order,
            from_city = models.City.objects.get(pk=request.POST.get('from_city')),
            to_city = random_city,
            price = random.randint(1000,3000),
            delivery_time = random.randint(2,20),
            # transport = random.choice(transport),
            )
        random_city2 = random.choice(city_list)
        models.OrderRoute.objects.create(
            order = order,
            from_city = random_city,
            to_city = random_city2,
            price = random.randint(1000,3000),
            delivery_time = random.randint(2,20),
            # transport = random.choice(transport),
            )

        models.OrderRoute.objects.create(
            order = order,
            from_city = random_city2,
            to_city = models.City.objects.get(pk=request.POST.get('to_city')),
            price = random.randint(1000,3000),
            delivery_time = random.randint(2,20),
            # transport = random.choice(transport),
            )

        return redirect('apply_order')


    context = {
        'city':city,
        'type':type,
    }

    return render(request, 'mainSite/make_order.html', context)


def apply_order(request):
    order = models.Order.objects.all().last()
    order_route = models.OrderRoute.objects.filter(order=order)

    context = {
        'order':order,
        'order_route':order_route,
    }
    return render(request, 'mainSite/apply_order.html', context) 

def cancel_order(request):
    models.Order.objects.all().last().delete()

    return redirect('home') 

def register(request):
    user_form = CreateUserForm

    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
                user_form.save()
                username = request.POST.get('username')
                password = request.POST.get('password1')
                user = authenticate(request, username=username, password=password)
                login(request,user)

                return redirect('home')

    context = {
        'user_form':user_form,
    }

    return render(request, 'mainSite/myAuth/register.html', context)



def login_page(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error = 'Проверьте введёные данные!'

    context = {
        "error":error,

    }
    return render(request, 'mainSite/myAuth/login.html', context)



def logout_view(request):
    logout(request)
    return redirect('home')


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializers
    queryset = models.Order.objects.all()


class RetriveTypeListView(generics.ListAPIView):
    serializer_class = RetriveTypeSerializers
    queryset = models.RetriveType.objects.all()


class OrderRouteListView(generics.ListAPIView):
    serializer_class = OrderRouteSerializers
    queryset = models.OrderRoute.objects.all()


class StatusListView(generics.ListAPIView):
    serializer_class = StatusSerializers
    queryset = models.Status.objects.all()


class TransportListView(generics.ListAPIView):
    serializer_class = TransportSerializers
    queryset = models.Transport.objects.all()

class CityListView(generics.ListAPIView):
    serializer_class = CitySerializers
    queryset = models.City.objects.all()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializers


class OrderRouteCreateView(generics.CreateAPIView):
    serializer_class = OrderRouteSerializers