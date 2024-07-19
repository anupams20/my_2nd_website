from django.contrib import admin
from .models import Itemlist

@admin.register(Itemlist)
class ItemlistAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount')
    search_fields = ('name',)
