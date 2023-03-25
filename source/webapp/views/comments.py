from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

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



