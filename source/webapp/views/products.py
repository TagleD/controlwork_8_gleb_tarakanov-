from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from webapp.forms import ProductForm
from webapp.models.product import Product


class IndexView(ListView):
    template_name = 'products_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ('-created_at',)


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Product



class ProductCreateView(SuccessMessageMixin, CreateView):
    template_name = 'product_add.html'
    model = Product
    form_class = ProductForm
    success_message = 'Товар успешно добавлен'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)

    # def get_success_url(self):
    #     # return reverse('product_detail', kwargs={'pk': self.object.pk})
    #     return reverse('index')

    # def form_valid(self, form):
    #     form = self.form_class(self.request.POST, self.request.FILES)
    #     return super().form_valid(form)
    #
    # def form_invalid(self, form):
    #     form = self.form_class(self.request.POST, self.request.FILES)
    #     return super().form_invalid(form)



    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST, request.FILES)
    #     context = {'form': form}
    #     return self.render_to_response(context)


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'product_update.html'
    model = Product
    form_class = ProductForm
    success_message = 'Товар успешно изменен'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.kwargs.get('pk')})

class ProductDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
    success_message = 'Товар успешно удален!'