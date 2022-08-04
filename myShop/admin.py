from django.contrib import admin
from myShop.models import Product, Category, Order, Cart, ProductAdmin, CategoryAdmin, OrderAdmin, CartAdmin

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)

