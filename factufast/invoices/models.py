from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.

class Product(models.Model):

    CURRENCIES = (
        ('COP', 'COP'),
        ('USD', 'USD'),
    )

    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency = models.CharField(choices=CURRENCIES, null=True, blank=True, default='COP', max_length=3)

    # Utility fields
    unique_id = models.UUIDField(
        default=uuid4, editable=False, unique=True, blank=True, null=True
    )
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now, blank=True, null=True)
    date_updated = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f"{self.title}, {self.unique_id}"

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.unique_id is None:
            self.unique_id = str(uuid4()).split("-")[4]
            self.slug = slugify(f"{self.title}-{self.unique_id}")

        self.slug = slugify(f"{self.title}-{self.unique_id}")
        self.date_updated = timezone.localtime(timezone.now())
        super(Product, self).save(*args, **kwargs)