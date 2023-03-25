from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from webapp.forms import CommentForm
from webapp.models import Comment, Product


class CommentCreateView(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    template_name = 'comments/comment_add.html'
    model = Comment
    form_class = CommentForm
    success_message = 'Комментарий успешно добавлен'
    permission_denied_message = 'У вас нет прав доступа'

    def test_func(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        comment = form.save(commit=False)
        comment.product = product
        comment.author = self.request.user
        comment.save()
        return redirect('product_detail', pk=product.pk)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        context['product'] = product
        return context


class CommentUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    template_name = 'comments/comment_update.html'
    model = Comment
    form_class = CommentForm
    success_message = 'Комментарий успешно изменен'
    permission_denied_message = 'У вас нет прав доступа'

    def test_func(self):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        return self.request.user.id == comment.author.id

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': Comment.objects.get(pk=self.kwargs.get('pk')).product.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        product = comment.product
        context['product'] = product
        return context

class CommentDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    template_name = 'comments/comment_confirm_delete.html'
    model = Comment
    success_message = 'Комментарий успешно удален!'

    def test_func(self):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        return self.request.user.id == comment.author.id

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': Comment.objects.get(pk=self.kwargs.get('pk')).product.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        product = comment.product
        context['product'] = product
        return context


