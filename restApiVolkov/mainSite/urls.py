"""ChinaApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),

    path('my_order/', views.my_order, name='my_order'),
    path('order_route/<int:pk>/', views.order_route, name='order_route'),
    path('make_order/', views.make_order, name='make_order'),
    path('cancel_order/', views.cancel_order, name='cancel_order'),
    path('apply_order/', views.apply_order, name='apply_order'),
    path('route/', views.route, name='route'),

    path('login_page/', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('api/v1/orders/', views.OrderListView.as_view()),
    path('api/v1/order_routes/', views.OrderRouteListView.as_view()),
    path('api/v1/create_order/', views.OrderCreateView.as_view()),
    path('api/v1/create_order_route/', views.OrderRouteCreateView.as_view()),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
