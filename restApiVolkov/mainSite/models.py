from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, unique=True, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы' 

class RouteStatus(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, unique=True, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус машрута'
        verbose_name_plural = 'Статусы маршрутов' 




class RetriveType(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Наименование')
    image = models.ImageField(verbose_name='Фото', upload_to='images/category/', null=True, blank=True)
    descripton = models.TextField(verbose_name='Описание', null=False, blank=False)
   

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип отправления'
        verbose_name_plural = 'Типы отправления' 


class Transport(models.Model):
    retrive_type = models.ForeignKey(RetriveType, verbose_name='Тип транспорта', on_delete=models.CASCADE)
    name = models.CharField(max_length=256, verbose_name='Наименование', null=False, blank=False)
    capacity = models.FloatField(null=True, blank=True, verbose_name='Грузоподъёмность')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорт' 



class City(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, unique=True, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города' 


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Имя', null=True, blank=True)
    second_name = models.CharField(max_length=50, verbose_name='Фамилия', null=True, blank=True)
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', null=True, blank=True)
    retrive_type = models.ForeignKey(RetriveType, verbose_name='Тип отправления',null=True, blank=True, on_delete=models.SET_NULL)
    delivery_name = models.CharField(max_length=255, verbose_name='Груз:', null=True, blank=True)
    weight = models.DecimalField(verbose_name='Вес',null=True, blank=True, max_digits=10, decimal_places=2)
    from_city = models.ForeignKey(City, verbose_name='Откуда', related_name='from_city_order',null=True, blank=True, on_delete=models.SET_NULL)
    to_city = models.ForeignKey(City, verbose_name='Куда', related_name='to_city_order',null=True, blank=True, on_delete=models.SET_NULL)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.SET_NULL, null=True, blank=True)
    # total_price = models.DecimalField(verbose_name='Общая стоимость',null=True, blank=True, default=0, max_digits=10, decimal_places=2)
    # total_time = models.IntegerField(null=True, blank=True, default=0, verbose_name='Общее время доставки')

    def __str__(self):
        return f'Заказ №{self.id} ({self.user})'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all()) + self.weight 

    def get_total_time(self):
        return sum(item.get_time() for item in self.items.all())

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы' 



class OrderRoute(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ', related_name='items', on_delete=models.CASCADE)
    from_city = models.ForeignKey(City, verbose_name='Откуда', related_name='from_city',null=True, blank=True, on_delete=models.SET_NULL)
    to_city = models.ForeignKey(City, verbose_name='Куда', related_name='to_city',null=True, blank=True, on_delete=models.SET_NULL)
    route_status = models.ForeignKey(RouteStatus, null=True, blank=True, verbose_name='Статус маршрута', on_delete=models.SET_NULL)
    price = models.DecimalField(verbose_name='Цена',null=True, blank=True, default=0, max_digits=10, decimal_places=2)
    delivery_time = models.IntegerField(null=True, blank=True, default=0, verbose_name='Время доставки')
    transport = models.ForeignKey(Transport,null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Транспорт')


    def __str__(self):
            return f'{self.order} / {self.from_city} / {self.to_city}'
    
    def get_cost(self):
        return self.price

    def get_time(self):
        return self.delivery_time

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты' 
