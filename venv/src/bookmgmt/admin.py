from django.contrib import admin
from .forms import InventoryCreateForm
from .models import Inventory


class InventoryCreateAdmin(admin.ModelAdmin):
    list_display = ['genre', 'bookname', 'quantity']
    form = InventoryCreateForm
    list_filter = ['genre']
    search_fields = ['genre', 'bookname']

admin.site.register(Inventory, InventoryCreateAdmin)