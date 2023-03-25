from django import forms
from django.core.exceptions import ValidationError

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
