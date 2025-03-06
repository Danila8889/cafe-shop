from django.urls import path, include

from cafe.api_v1.urls import api_router
from .views import OrderDetailsView, OrdersListView, OrderUpdate, CreateOrder, OrderDelete, TableDetail, \
    OrdersTotalPrice

app_name = "cafe"

urlpatterns = [
    # orders crud
    path("orders/", OrdersListView.as_view(), name="orders_list"),
    path("orders/total_price", OrdersTotalPrice.as_view(), name="total_price"),
    path("orders/create", CreateOrder.as_view(), name="create"),
    path("order/<int:pk>/detail/", OrderDetailsView.as_view(), name="order"),
    path("order/<int:pk>/update/", OrderUpdate.as_view(), name="update"),
    path("order/<int:pk>/delete/", OrderDelete.as_view(), name="delete"),

    # tables
    path("table/<int:pk>/detail/", TableDetail.as_view(), name="table"),

    # api router
    path("api/", include(api_router.urls))
]
