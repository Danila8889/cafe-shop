from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from cafe.models import Order, Table
from .forms import OrderForm
from .mixins import Error404Mixin


class OrdersListView(ListView):
    template_name = "cafe/orders/orders_list.html"
    queryset = Order.objects.all().prefetch_related("items")
    context_object_name = "orders"


class OrdersTotalPrice(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        total_price = sum([order.total_price for order in Order.objects.all()])
        return HttpResponse(f"total_price orders: {total_price}")


class CreateOrder(CreateView):
    template_name = "cafe/orders/create_order.html"
    context_object_name = 'order'
    form_class = OrderForm

    def get_success_url(self):
        return reverse("cafe:order", kwargs={"pk": self.object.pk})


class OrderDetailsView(Error404Mixin, DetailView):
    template_name = "cafe/orders/order_details.html"
    queryset = Order.objects.all().prefetch_related("items")
    context_object_name = "order"


class OrderUpdate(Error404Mixin, UpdateView):
    template_name = 'cafe/orders/order_update.html'
    queryset = Order.objects.all().prefetch_related("items")
    context_object_name = 'order'
    form_class = OrderForm

    def get_success_url(self):
        return reverse("cafe:order", kwargs={"pk": self.object.pk})


class OrderDelete(Error404Mixin, DeleteView):
    template_name = 'cafe/orders/order_delete.html'
    queryset = Order.objects.all().prefetch_related("items")
    context_object_name = 'order'

    def get_success_url(self):
        return reverse("cafe:orders_list")


class TablesListView(ListView):
    template_name = "cafe/tables/tables_list.html"
    queryset = Table.objects.all().prefetch_related("orders")
    context_object_name = "tables"


class TableDetail(Error404Mixin, DetailView):
    template_name = "cafe/tables/table_details.html"
    queryset = Table.objects.all().prefetch_related("orders")
    context_object_name = "table"
