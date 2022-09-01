
from django.contrib import admin
from django.urls import path
from accounts.views import signup, login_view, logout_view
from myShop.views import index, details, add_to_cart, cart, delete_cart, contact, profile
from djangoProject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("details/", details, name="details"),
    path('product/<str:slug>/', details, name='product'),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('cart/', cart, name='cart'),
    path('product/<str:slug>/add_to_cart/', add_to_cart, name='add-to-cart'),
    path('delete-cart/', delete_cart, name='delete-cart'),
    path('contact/', contact, name='contact'),
    path('profile/', profile, name='myprofile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
