from django.db import models


# Create your models here.
class MainCategory(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Название категории'
        verbose_name_plural = 'Названия категорий'
        ordering = ['-title']

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title_sub = models.CharField(max_length=50, verbose_name='Название подкатегории')
    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Название подкатегории'
        verbose_name_plural = 'Названия подкатегорий'
        # ordering = ['-title_sub']

    def __str__(self):
        return self.title_sub
