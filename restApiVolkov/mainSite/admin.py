from django.contrib import admin
from . import models

# Register your models here.
class TransportInline(admin.TabularInline):
    model = models.Transport


class TransportAdmin(admin.ModelAdmin):
    inlines = [TransportInline]

admin.site.register(models.RetriveType, TransportAdmin)

class OrderRouteInline(admin.TabularInline):
    model = models.OrderRoute


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderRouteInline]

admin.site.register(models.Order, OrderAdmin)

admin.site.register(models.Status)

admin.site.register(models.City)
admin.site.register(models.RouteStatus)