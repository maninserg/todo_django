from django.contrib import admin
from .models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')
    search_fields = ('text',)

admin.site.register(Item, ItemAdmin)
