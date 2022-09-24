from django.contrib import admin

from .models import Invoice, Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "quantity", "price", "currency"]
    list_filter = ["currency"]
    search_fields = ["title", "description", "currency"]
    list_per_page = 25


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["client", "payment_terms", "status"]
    list_filter = ["payment_terms", "status"]
    search_fields = ["client", "payment_terms", "status"]
    list_per_page = 25
