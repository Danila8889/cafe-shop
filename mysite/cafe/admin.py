from django.contrib import admin

from cafe.models import Item, Table, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    pass


class ItemsInline(admin.StackedInline):
    model = Order.items.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ItemsInline,
    ]
    list_display = 'table_number', 'total_price', 'status'
