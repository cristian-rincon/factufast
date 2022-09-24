from uuid import uuid4

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

from factufast.users.models import Client

# Create your models here.


class Product(models.Model):

    CURRENCIES = (
        ("COP", "COP"),
        ("USD", "USD"),
    )

    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency = models.CharField(
        choices=CURRENCIES, null=True, blank=True, default="COP", max_length=3
    )

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


class Invoice(models.Model):

    one_month = "30 Días"
    TERMS_OPTIONS = (
        ("15 Días", "15 Días"),
        (one_month, one_month),
        ("45 Días", "45 Días"),
        ("60 Días", "60 Días"),
    )

    STATUS_OPTIONS = (
        ("Pendiente", "Pendiente"),
        ("Pagado", "Pagado"),
        ("Cancelado", "Cancelado"),
        ("Vencido", "Vencido"),
    )

    # Invoice info
    title = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=100, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    payment_terms = models.CharField(
        choices=TERMS_OPTIONS, null=True, blank=True, default=one_month, max_length=10
    )
    status = models.CharField(
        choices=STATUS_OPTIONS,
        null=True,
        blank=True,
        default="Pendiente",
        max_length=10,
    )
    notes = models.TextField(null=True, blank=True)

    # Relation fields
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True
    )

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
        return reverse("invoice-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.unique_id is None:
            self.unique_id = str(uuid4()).split("-")[4]
            self.slug = slugify(f"{self.title}-{self.unique_id}")

        self.slug = slugify(f"{self.title}-{self.unique_id}")
        self.date_updated = timezone.localtime(timezone.now())
        super(Invoice, self).save(*args, **kwargs)
