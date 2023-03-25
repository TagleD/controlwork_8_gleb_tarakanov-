from django.views.generic import ListView

from webapp.models.product import Product


class IndexView(ListView):
    template_name = 'products_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ('-created_at',)
