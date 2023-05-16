from django.db import models
from categories.models import SubCategory


# Create your models here.
class Condition(models.Model):
    title = models.CharField(max_length=50, verbose_name='Состояние')

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'

    def __str__(self):
        return self.title


class Size(models.Model):
    size = models.IntegerField(verbose_name='Размер обуви')

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return f'{self.size}'


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название товара')
    price = models.FloatField(null=False, blank=False, verbose_name='Цена')
    description = models.TextField(null=True, blank=True, verbose_name='Описание товара')
    # characteristic = models.ForeignKey(Сharacteristic, on_delete=models.CASCADE, verbose_name='Характеристики обуви')
    type_shoes = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Тип обуви')
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, verbose_name='Состояние обуви')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name='Размер обуви')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
