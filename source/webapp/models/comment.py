from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices


class RatingChoice(TextChoices):
    ZERO = '0', '0'
    ONE = '1', '1'
    TWO = '2', '2'
    THREE = '3', '3'
    FOUR = '4', '4'
    FIVE = '5', '5'

class Comment(models.Model):
    author = models.ForeignKey(
        to=get_user_model(),
        related_name='user_comments',
        verbose_name='Комментарий',
        null=False,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to='webapp.Product',
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    text = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
        verbose_name='Текст',
    )
    rating = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Рейтинг',
        choices=RatingChoice.choices,
        default=RatingChoice.FIVE
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время"
    )

    def __str__(self):
        return f'{self.author} - {self.text[:25]}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
