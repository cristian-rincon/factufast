from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for factufast.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Client(models.Model):

    COLOMBIA_CITIES = (
        ("Bogota", "Bogota"),
        ("Madrid", "Madrid"),
        ("Medellin", "Medellin"),
        ("Cali", "Cali"),
    )

    # Client info
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    logo = models.ImageField(default="default_logo.png", upload_to="client_logos")
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(
        choices=COLOMBIA_CITIES, max_length=100, null=True, blank=True
    )
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    tax_number = models.CharField(max_length=200, null=True, blank=True)

    # Utility fields
    unique_id = models.UUIDField(
        default=uuid4, editable=False, unique=True, blank=True, null=True
    )
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now, blank=True, null=True)
    date_updated = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.city}, {self.unique_id}"

    def get_absolute_url(self):
        return reverse("client-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.unique_id is None:
            self.unique_id = str(uuid4()).split("-")[4]
            self.slug = slugify(f"{self.name}-{self.unique_id}-{self.city}")

        self.slug = slugify(f"{self.name}-{self.unique_id}-{self.city}")
        self.date_updated = timezone.localtime(timezone.now())
        super(Client, self).save(*args, **kwargs)


class Setting(models.Model):

    COLOMBIA_CITIES = (
        ("Bogota", "Bogota"),
        ("Madrid", "Madrid"),
        ("Medellin", "Medellin"),
        ("Cali", "Cali"),
    )

    # SettingsUser info
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    logo = models.ImageField(default="default_logo.png", upload_to="company_logos")
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(
        choices=COLOMBIA_CITIES, max_length=100, null=True, blank=True
    )
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    tax_number = models.CharField(max_length=200, null=True, blank=True)

    # Utility fields
    unique_id = models.UUIDField(
        default=uuid4, editable=False, unique=True, blank=True, null=True
    )
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now, blank=True, null=True)
    date_updated = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.city}, {self.unique_id}"

    def get_absolute_url(self):
        return reverse("settings-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.unique_id is None:
            self.unique_id = str(uuid4()).split("-")[4]
            self.slug = slugify(f"{self.name}-{self.unique_id}-{self.city}")

        self.slug = slugify(f"{self.name}-{self.unique_id}-{self.city}")
        self.date_updated = timezone.localtime(timezone.now())
        super(Setting, self).save(*args, **kwargs)
