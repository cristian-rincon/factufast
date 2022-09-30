from uuid import uuid4

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone


class Client(models.Model):

    DEPARTMENTS = [
        ("BOG", "Bogota"),
        ("ANT", "Antioquia"),
        ("ATL", "Atlantico"),
        ("BOL", "Bolivar"),
    ]

    # Basic Fields.
    clientName = models.CharField(null=True, blank=True, max_length=200)
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    clientLogo = models.ImageField(
        default="default_logo.jpg", upload_to="company_logos"
    )
    department = models.CharField(choices=DEPARTMENTS, blank=True, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=10)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    emailAddress = models.CharField(null=True, blank=True, max_length=100)
    taxNumber = models.CharField(null=True, blank=True, max_length=100)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.clientName} {self.department} {self.uniqueId}"

    def get_absolute_url(self):
        return reverse("client-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split("-")[4]
            self.slug = slugify(f"{self.clientName} {self.department} {self.uniqueId}")

        self.slug = slugify(f"{self.clientName} {self.department} {self.uniqueId}")
        self.last_updated = timezone.localtime(timezone.now())

        super().save(*args, **kwargs)


class Invoice(models.Model):
    TERMS = [
        ("15 Dias", "15 Dias"),
        ("30 Dias", "30 Dias"),
        ("45 Dias", "45 Dias"),
        ("60 Dias", "60 Dias"),
        ("90 Dias", "90 Dias"),
    ]

    STATUS = [
        ("Borrador", "Borrador"),
        ("Enviado", "Enviado"),
        ("Pagado", "Pagado"),
        ("Cancelado", "Cancelado"),
        ("Vencido", "Vencido"),
    ]

    title = models.CharField(null=True, blank=True, max_length=100)
    number = models.CharField(null=True, blank=True, max_length=100)
    dueDate = models.DateField(null=True, blank=True)
    paymentTerms = models.CharField(choices=TERMS, default="15 Dias", max_length=100)
    status = models.CharField(choices=STATUS, default="Borrador", max_length=100)
    notes = models.TextField(null=True, blank=True)

    # RELATED fields
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.number} {self.uniqueId}"

    def get_absolute_url(self):
        return reverse("invoice-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split("-")[4]
            self.slug = slugify(f"{self.number} {self.uniqueId}")

        self.slug = slugify(f"{self.number} {self.uniqueId}")
        self.last_updated = timezone.localtime(timezone.now())

        super().save(*args, **kwargs)


class Product(models.Model):
    CURRENCY = [
        ("USD", "USD"),
        ("COP", "COP"),
    ]

    title = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency = models.CharField(choices=CURRENCY, default="COP", max_length=100)

    # Related Fields
    invoice = models.ForeignKey(
        Invoice, blank=True, null=True, on_delete=models.CASCADE
    )

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.uniqueId}"

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split("-")[4]
            self.slug = slugify(f"{self.title} {self.uniqueId}")

        self.slug = slugify(f"{self.title} {self.uniqueId}")
        self.last_updated = timezone.localtime(timezone.now())

        super().save(*args, **kwargs)


class Settings(models.Model):

    DEPARTMENTS = [
        ("Gauteng", "Gauteng"),
        ("Free State", "Free State"),
        ("Limpopo", "Limpopo"),
    ]

    # Basic Fields
    clientName = models.CharField(null=True, blank=True, max_length=200)
    clientLogo = models.ImageField(
        default="default_logo.jpg", upload_to="company_logos"
    )
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    department = models.CharField(choices=DEPARTMENTS, blank=True, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=10)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    emailAddress = models.CharField(null=True, blank=True, max_length=100)
    taxNumber = models.CharField(null=True, blank=True, max_length=100)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.clientName} {self.department} {self.uniqueId}"

    def get_absolute_url(self):
        return reverse("settings-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split("-")[4]
            self.slug = slugify(f"{self.clientName} {self.department} {self.uniqueId}")

        self.slug = slugify(f"{self.clientName} {self.department} {self.uniqueId}")
        self.last_updated = timezone.localtime(timezone.now())

        super().save(*args, **kwargs)
