from django.db import models
from django.db.models import TextChoices


class CategoryChoice(TextChoices):
    OTHER = 'OTHER', 'Другое'
    RIFLES = 'RIFLES', 'Винтовки'
    MELEE = 'MELEE', 'Ближнее'
    PISTOLS = 'PISTOLS', 'Пистолеты'
    SNIPERS = 'SNIPERS', 'Снайперские'


class Product(models.Model):
    name = models.CharField(
        max_length=40,
        blank=False,
        null=False,
        verbose_name='Наименование'
    )
    category = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Категория',
        choices=CategoryChoice.choices,
        default=CategoryChoice.OTHER
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='post_images',
        null=True,
        blank=True,
        verbose_name='Фото'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время",
        null=True
    )

    def __str__(self):
        return f'{self.name} = {self.category}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
