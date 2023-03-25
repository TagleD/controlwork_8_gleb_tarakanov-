from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from webapp.forms import CommentForm
from webapp.models import Comment, Product


class CommentCreateView(SuccessMessageMixin, CreateView):
    template_name = 'comments/comment_add.html'
    model = Comment
    form_class = CommentForm
    success_message = 'Комментарий успешно добавлен'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        comment = form.save(commit=False)
        comment.product = product
        print(self.request.user)
        comment.author = self.request.user
        comment.save()
        return redirect('product_detail', pk=product.pk)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        context['product'] = product
        return context


class CommentUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'comments/comment_update.html'
    model = Comment
    form_class = CommentForm
    success_message = 'Комментарий успешно изменен'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': Comment.objects.get(pk=self.kwargs.get('pk')).product.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        product = comment.product
        context['product'] = product
        return context



