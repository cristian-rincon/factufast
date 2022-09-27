from django.urls import path
from invoices import views

urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("clients", views.ClientListView.as_view(), name="clients"),
    path("client/create", views.ClientCreateView.as_view(), name="create_client"),
    path("client/<str:slug>", views.ClientDetailView.as_view(), name="client_detail"),
    path("client/<str:slug>/update", views.ClientUpdateView.as_view(), name="update_client"),
]
