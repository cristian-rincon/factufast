# import login_required decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from factufast.invoices.forms import ClientForm, ProductForm
from factufast.invoices.models import Client, Product

# Create your views here.


@login_required
def dashboard(request):
    context = {}
    return render(request, "invoices/dashboard.html", context)


# Client views


class ClientListView(LoginRequiredMixin, ListView):
    template_name = "invoices/client/list.html"
    model = Client
    context_object_name = "clients"
    ordering = ("-date_created",)
    paginate_by = 30


# Client Detail View


class ClientDetailView(LoginRequiredMixin, DetailView):
    template_name = "invoices/client/detail.html"
    queryset = Client.objects.all()
    context_object_name = "client"


# Client Create View


class ClientCreateView(LoginRequiredMixin, CreateView):
    def get(self, request, *args, **kwargs):
        form = ClientForm()
        return render(request, "invoices/client/create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy("invoices:clients"))
        return render(request, "invoices/client/create.html", {"form": form})


# Client Update View


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "invoices/client/update.html"
    queryset = Client.objects.all()
    form_class = ClientForm

    def get_object(self):
        slug = self.kwargs.get("slug")
        return Client.objects.get(slug=slug)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("invoices:clients")


# Product Views


class ProductListView(LoginRequiredMixin, ListView):
    template_name = "invoices/product/list.html"
    model = Product
    context_object_name = "products"
    ordering = ("-date_created",)
    paginate_by = 30


# Product Detail View


class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = "invoices/product/detail.html"
    queryset = Product.objects.all()
    context_object_name = "product"


# Product Create View


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = "invoices/product/create.html"
    queryset = Product.objects.all()
    form_class = ProductForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("invoices:products")


# Product Update View


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "invoices/product/update.html"
    queryset = Product.objects.all()
    form_class = ProductForm

    def get_object(self):
        slug = self.kwargs.get("slug")
        return Product.objects.get(slug=slug)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("invoices:products")


# Product Delete View


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "invoices/product/delete.html"
    queryset = Product.objects.all()
    form_class = ProductForm

    def get_object(self):
        slug = self.kwargs.get("slug")
        return Product.objects.get(slug=slug)

    def get_success_url(self):
        return reverse_lazy("invoices:products")
