from rest_framework.routers import DefaultRouter

from cafe.api_v1.api_view import OrdersListAPI
api_router = DefaultRouter()
api_router.register('orders', OrdersListAPI, basename='api_orders')
