from django.urls import path

from factufast.invoices import views

urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    # Client urls
    path("clients", views.ClientListView.as_view(), name="clients"),
    path("client/create", views.ClientCreateView.as_view(), name="create_client"),
    path("client/<str:slug>", views.ClientDetailView.as_view(), name="client_detail"),
    path(
        "client/<str:slug>/update",
        views.ClientUpdateView.as_view(),
        name="update_client",
    ),
    # Product urls
    path("products", views.ProductListView.as_view(), name="products"),
    path("product/create", views.ProductCreateView.as_view(), name="create_product"),
    path(
        "product/<str:slug>", views.ProductDetailView.as_view(), name="product_detail"
    ),
    path(
        "product/<str:slug>/update",
        views.ProductUpdateView.as_view(),
        name="update_product",
    ),
    path(
        "product/<str:slug>/delete",
        views.ProductDeleteView.as_view(),
        name="delete_product",
    ),
]
