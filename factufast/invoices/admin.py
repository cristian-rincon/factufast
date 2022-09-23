from django.contrib import admin
from .models import Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "quantity", "price", "currency"]
    list_filter = ["currency"]
    search_fields = ["title", "description", "currency"]
    list_per_page = 25
