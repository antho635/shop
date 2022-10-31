from django.contrib import admin
from django.db import models
from django.urls import reverse
from djangoProject.settings import AUTH_USER_MODEL

'''
Category model
- title: name of the category (CharField)
- description: description of the category (TextField)
'''


class Category(models.Model):
    title = models.CharField(max_length=120)
    date_added = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['-date_added']


'''
Product model
- name: name of the product (CharField)
- slug: slug of the product (SlugField)
- price: price of the product (FloatField)
- category: category of the product (ForeignKey)
- description: description of the product (TextField)
- image: image of the product (ImageField)
- stock: stock of the product (IntegerField)
'''


class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=520, unique=True)
    price = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=2500)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    stock = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-date_added"]


'''
Order model
- user: user of the order (ForeignKey)
- product: product of the order (ForeignKey)
- quantity: quantity of the order (IntegerField)
- ordered: ordered of the order (BooleanField)
- date_ordered: date of the order (DateTimeField)
    class Meta:
        ordering = ['-date_ordered']    
'''


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} ({self.user.username}) ({self.quantity}) ({self.ordered_date})"

    class Meta:
        ordering = ['-ordered_date']


'''
Cart model
- user: user of the cart (ForeignKey)
- orders: orders of the cart (ManyToManyField)
- ordered: ordered of the cart (BooleanField)
- ordered_date: ordered_date of the cart (DateTimeField)
- quantity: quantity of the cart (IntegerField)
'''


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order, blank=True)

    def __str__(self):
        return f"{self.user.name} + 's cart + ' ' + self.quantity"

    class Meta:
        ordering = ['-user']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_added']
    list_filter = ['date_added']
    ordering = ['-date_added']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['slug', 'price', 'stock', 'date_added']
    list_filter = ['date_added']
    ordering = ['-date_added']


class CartAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


class Contact(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(max_length=2500, blank=True, null=True)
    date_send = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_send']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_send']
    list_filter = ['date_send']
    ordering = ['-date_send']


class UserProfile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=120, blank=True, null=True)
    phone = models.CharField(max_length=120, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    zipcode = models.CharField(max_length=120, blank=True, null=True)
    image_profile = models.ImageField(upload_to='profile_image', blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = "UserProfiles"
        verbose_name = "UserProfile"

    def is_valid(self):
        pass


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'username', 'phone', 'address', 'city', 'state', 'zipcode', 'date_added']
    list_filter = ['date_added']
    ordering = ['-date_added']
