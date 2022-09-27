from django import forms
from factufast.invoices.models import Invoice, Product, Client
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row



class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            "title",
            "number",
            "due_date",
            "payment_terms",
            "status",
            "notes",
            "client",
            "products",
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "quantity", "price", "currency"]


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "name",
            "address",
            "logo",
            "postal_code",
            "city",
            "phone_number",
            "email",
            "tax_number",
        ]
  
