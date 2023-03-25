from django.contrib import admin

from webapp.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'image')
    list_filter = ('id', 'name', 'category', 'description')
    search_fields = ('id', 'name', 'category', 'description')
    fields = ('id', 'name', 'category', 'description')
    readonly_fields = ('id',)

admin.site.register(Product, ProductAdmin)
