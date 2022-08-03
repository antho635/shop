from django.contrib import admin
from django.urls import path
from myShop.views import index, details
from djangoProject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("details/", details, name="details"),
    path('product/<str:slug>/', details, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
