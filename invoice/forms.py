# Form Layout from Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.contrib.auth.models import User

from .models import Client, Invoice, Product, Settings


class DateInput(forms.DateInput):
    input_type = "date"


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"id": "floatingInput", "class": "form-control mb-3"}
        ),
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"id": "floatingPassword", "class": "form-control mb-3"}
        ),
        required=True,
    )

    class Meta:
        model = User
        fields = ["username", "password"]


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "clientName",
            "clientLogo",
            "addressLine1",
            "department",
            "postalCode",
            "phoneNumber",
            "emailAddress",
            "taxNumber",
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "quantity", "price", "currency"]


class InvoiceForm(forms.ModelForm):
    THE_OPTIONS = [
        ("15 Dias", "15 Dias"),
        ("30 Dias", "30 Dias"),
        ("45 Dias", "45 Dias"),
        ("60 Dias", "60 Dias"),
        ("90 Dias", "90 Dias"),
    ]
    STATUS_OPTIONS = [
        ("Borrador", "Borrador"),
        ("Enviado", "Enviado"),
        ("Pagado", "Pagado"),
        ("Cancelado", "Cancelado"),
        ("Vencido", "Vencido"),
    ]

    title = forms.CharField(
        required=True,
        label="Ttulo de la factura",
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Título de la factura"}
        ),
    )
    paymentTerms = forms.ChoiceField(
        choices=THE_OPTIONS,
        required=True,
        label="Terminos de pago",
        widget=forms.Select(attrs={"class": "form-control mb-3"}),
    )
    status = forms.ChoiceField(
        choices=STATUS_OPTIONS,
        required=True,
        label="Estado",
        widget=forms.Select(attrs={"class": "form-control mb-3"}),
    )
    notes = forms.CharField(
        required=True,
        label="Notas",
        widget=forms.Textarea(attrs={"class": "form-control mb-3"}),
    )

    dueDate = forms.DateField(
        required=True,
        label="Fecha de vencimiento",
        widget=DateInput(attrs={"class": "form-control mb-3"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("title", css_class="form-group col-md-6"),
                Column("dueDate", css_class="form-group col-md-6"),
                css_class="form-row",
            ),
            Row(
                Column("paymentTerms", css_class="form-group col-md-6"),
                Column("status", css_class="form-group col-md-6"),
                css_class="form-row",
            ),
            "notes",
            Submit("submit", "Guardar"),
        )

    class Meta:
        model = Invoice
        fields = ["title", "dueDate", "paymentTerms", "status", "notes"]


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = [
            "clientName",
            "clientLogo",
            "addressLine1",
            "department",
            "postalCode",
            "phoneNumber",
            "emailAddress",
            "taxNumber",
        ]


class ClientSelectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.initial_client = kwargs.pop("initial_client")
        self.CLIENT_LIST = Client.objects.all()
        self.CLIENT_CHOICES = [("-----", "Seleccione un cliente")]

        for client in self.CLIENT_LIST:
            d_t = (client.uniqueId, client.clientName)
            self.CLIENT_CHOICES.append(d_t)

        super().__init__(*args, **kwargs)

        self.fields["client"] = forms.ChoiceField(
            label="Cliente",
            choices=self.CLIENT_CHOICES,
            widget=forms.Select(attrs={"class": "form-control mb-3"}),
        )

    class Meta:
        model = Invoice
        fields = ["client"]

    def clean_client(self):
        c_client = self.cleaned_data["client"]
        if c_client == "-----":
            return self.initial_client
        else:
            return Client.objects.get(uniqueId=c_client)
