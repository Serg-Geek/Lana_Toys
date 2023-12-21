from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='Тестовый товар', description='Описание', price=100.00)

    def test_str_method(self):
        product = Product.objects.get(id=1)
        expected_str = product.name
        self.assertEqual(expected_str, str(product))



