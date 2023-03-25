from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from webapp.forms import ProductForm
from webapp.models.product import Product


class IndexView(ListView):
    template_name = 'products/products_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ('-created_at',)
    paginate_orphans = 1
    paginate_by = 2


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        return context


class ProductCreateView(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    template_name = 'products/product_add.html'
    model = Product
    form_class = ProductForm
    success_message = 'Товар успешно добавлен'
    success_url = '/'
    permission_denied_message = 'У вас нет прав доступа'

    def test_func(self):
        return self.request.user.has_perm('webapp.add_product')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class ProductUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    template_name = 'products/product_update.html'
    model = Product
    form_class = ProductForm
    success_message = 'Товар успешно изменен'
    permission_denied_message = 'У вас нет прав доступа'

    def test_func(self):
        return self.request.user.has_perm('webapp.change_product')

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.kwargs.get('pk')})


class ProductDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    template_name = 'products/product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
    success_message = 'Товар успешно удален!'
    permission_denied_message = 'У вас нет прав доступа'

    def test_func(self):
        return self.request.user.has_perm('webapp.delete_product')

