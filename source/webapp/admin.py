from django.contrib import admin

from webapp.models import Product
from webapp.models.comment import Comment


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'image')
    list_filter = ('id', 'name', 'category', 'description')
    search_fields = ('id', 'name', 'category', 'description')
    fields = ('id', 'name', 'category', 'description')
    readonly_fields = ('id',)

admin.site.register(Product, ProductAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'text', 'rating')
    list_filter = ('id', 'author', 'product', 'text', 'rating')
    search_fields = ('id', 'author', 'product', 'text', 'rating')
    fields = ('id', 'author', 'product', 'text', 'rating')
    readonly_fields = ('id',)

admin.site.register(Comment, CommentAdmin)

