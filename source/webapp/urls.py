from django.urls import path

from webapp.views.comments import CommentCreateView, CommentUpdateView
from webapp.views.products import IndexView, ProductCreateView, ProductUpdateView, ProductDetailView, ProductDeleteView



urlpatterns = [
    # URLS для продуктов
    path('', IndexView.as_view(), name='index'),
    path('product/add', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/detail', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/confirm_delete/', ProductDeleteView.as_view(), name='confirm_delete'),

    # URLS для комментариев
    path('product/<int:pk>/comment/add', CommentCreateView.as_view(), name='product_add_comment'),
    path('product/comment/<int:pk>/update', CommentUpdateView.as_view(), name='product_update_comment')
]
