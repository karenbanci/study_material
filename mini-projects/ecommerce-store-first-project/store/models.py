from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    # here we define the fields for the Category model
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="product", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name="product_creator", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="admin")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    # será desligado uma vez ou adicionado uma vez quando o produto for criado
    created = models.DateTimeField(auto_now_add=True)
    # toda vez que fizer atualização no produto, será atualizado a data
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Products"
        # ordenar os produtos por data de criação, negativo para ordem decrescente
        ordering = ("-created",)

    def __str__(self):
        return self.title
