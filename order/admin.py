from django.contrib import admin

# Register your models here.

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)
