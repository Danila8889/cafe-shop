from rest_framework import viewsets

from cafe.models import Order
from cafe.api_v1.order_serializer import OrderSerializer


class OrdersListAPI(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
