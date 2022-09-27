from django.contrib import admin

from .models import Invoice, Product, Client, Setting

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


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "city", "phone_number", "email"]
    list_filter = ["city"]
    search_fields = ["name", "city", "phone_number", "email"]
    list_per_page = 25


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "city", "phone_number", "email"]
    list_filter = ["city"]
    search_fields = ["name", "city", "phone_number", "email"]
    list_per_page = 25
