from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Comment
from webapp.models.product import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'image')
        labels = {
            'name': 'Наименование товара',
            'category': 'Выберите категорию из списка',
            'description': 'Описание товара',
            'image': 'Фото товара'
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError('Наименование должно быть длинее 2-ух символов')
        return name


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'rating')
        labels = {
            'text': 'Напишите отзыв',
            'rating': 'Поставьте оценку товару',
        }

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 2:
            raise ValidationError('Отзыв должен быть длинее 20-ти символов')
        return text
