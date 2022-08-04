from django.db import models
from django.urls import reverse
from djangoProject import settings
from djangoProject.settings import AUTH_USER_MODEL

'''
Category model
- title: name of the category (CharField)
- description: description of the category (TextField)
'''


class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=2500)

    def __str__(self):
        return self.title


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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})


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
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name},(Utilisateur : {self.user.username}, Quantité : {self.quantity})"

    class Meta:
        ordering = ['-date_ordered']



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
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s cart", self.quantity

    class Meta:
        ordering = ['-ordered_date']
