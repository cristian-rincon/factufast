# import login_required decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render

from django.http import HttpResponseRedirect

from factufast.invoices.models import Client
from factufast.invoices.forms import ClientForm
# Create your views here.

from django.urls import reverse_lazy


@login_required
def dashboard(request):
    context = {}
    return render(request, "invoices/dashboard.html", context)


# Client views

class ClientListView(LoginRequiredMixin, ListView):
    template_name = "invoices/client/list.html"
    model = Client
    context_object_name = "clients"
    ordering = ('-date_created',)
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
        return render(request, 'invoices/client/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('invoices:clients'))
        return render(request, 'invoices/client/create.html', {'form': form})

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
