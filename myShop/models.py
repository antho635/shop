from django.db import models
from django.urls import reverse
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
'''

'''
Cart model
- user: user of the cart (ForeignKey)
- orders: orders of the cart (ManyToManyField)
- ordered: ordered of the cart (BooleanField)
- ordered_date: ordered_date of the cart (DateTimeField)
- quantity: quantity of the cart (IntegerField)
'''
