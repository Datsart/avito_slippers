from django.db import models


# Create your models here.


class Pattern(models.Model):
    pattern = models.CharField(max_length=50, verbose_name='Состояние')

    class Meta:
        verbose_name = 'Состояние обуви'
        verbose_name_plural = 'Состояния обуви'

    def __str__(self):
        return self.pattern

# class Size(models.Model):
#     size =
class TypeShoses(models.Model):
    type = models.CharField(max_length=50, verbose_name='Тип обуви')

    class Meta:
        verbose_name = 'Тип обуви'
        verbose_name_plural = 'Типы обуви'

    def __str__(self):
        return self.type


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название товара')
    price = models.FloatField(null=False, blank=False, verbose_name='Цена')
    adress = models.CharField(max_length=100, verbose_name='Адрес')
    characteristics = models.ForeignKey(TypeShoses, null=True, blank=True, verbose_name='Тип обуви',
                                        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
