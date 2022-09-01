from django.contrib import admin
from myShop.models import Product, Category, Order, Cart, ProductAdmin, CategoryAdmin, OrderAdmin, CartAdmin, Contact, \
    ContactAdmin, UserProfile, UserProfileAdmin


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(UserProfile, UserProfileAdmin)


