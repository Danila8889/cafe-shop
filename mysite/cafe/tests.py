import io

from django.test import TestCase
from django.urls import reverse
from rest_framework.parsers import JSONParser

from cafe.models import Order, Item, Table

STATUS_CHOICES = [
    ('pending', 'В ожидании'),
    ('ready', 'Готово'),
    ('paid', 'Оплачено'),
]


class CreateAndGetOrderTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.table = Table.objects.create(number=8)
        cls.item = Item.objects.create(name='fish', description='sweet', price=12, discount=2, archived=False)
        cls.order = Order.objects.create(table_number=cls.table, total_price=60, status=STATUS_CHOICES[0])
        cls.order.items.set([cls.item])

    @classmethod
    def tearDownClass(cls):
        cls.table.delete()
        cls.item.delete()
        cls.order.delete()

    def test_get_order(self):
        res = self.client.get(reverse('cafe:order', kwargs={"pk": self.order.pk}))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.order.pk)
        self.assertContains(res, self.order.table_number.number)
        self.assertContains(res, self.order.total_price)


class GetOrdersListFromDBTestCase(TestCase):
    fixtures = ['items-fixture.json', 'orders-fixture.json', 'tables-fixture.json']

    # делаем мок БД, имитируя реальные записи items, orders и tables
    def test_orders_list(self):
        self.assertEqual(1, 1)
        res = self.client.get(reverse('cafe:orders_list'))
        orders = Order.objects.all().order_by('pk')
        self.assertQuerySetEqual(qs=orders,
                                 values=(p.pk for p in res.context["orders"]),
                                 transform=lambda p: p.pk)
        self.assertTemplateUsed(res, 'cafe/orders/orders_list.html')


class SummTotalPriceTestCase(TestCase):
    fixtures = ['items-fixture.json', 'orders-fixture.json', 'tables-fixture.json']

    def test_total_price_summ(self):
        res = self.client.get(reverse('cafe:total_price'))
        total_price_orders = sum([order.total_price for order in Order.objects.all()])
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, total_price_orders)


class OrdersAPITestCase(TestCase):
    fixtures = ['items-fixture.json', 'orders-fixture.json', 'tables-fixture.json']

    def test_api_orders_list(self):
        res = self.client.get(reverse('cafe:api_orders-list'))
        self.assertEqual(res.status_code, 200)
        res = io.BytesIO(res.content)
        data = JSONParser().parse(res)
        orders_db = Order.objects.all().order_by('id')
        self.assertQuerySetEqual(qs=orders_db,
                                 values=(p.get('id') for p in data),
                                 transform=lambda p: p.pk)


class CreateAndGetTableTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.table = Table.objects.create(number=17)

    @classmethod
    def tearDownClass(cls):
        cls.table.delete()

    def test_get_table(self):
        res = self.client.get(reverse('cafe:table', kwargs={"pk": self.table.pk}))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.table.pk)
        self.assertContains(res, self.table.number)
        self.assertTemplateUsed(res, 'cafe/tables/table_details.html')
