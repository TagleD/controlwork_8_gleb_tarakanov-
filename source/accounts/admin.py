from django.contrib import admin

from accounts.models import Account


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Account, AccountAdmin)