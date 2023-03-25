from django.urls import path

from webapp.views.products import IndexView, ProductCreateView, ProductUpdateView, ProductDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/add', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/detail', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update')
]
