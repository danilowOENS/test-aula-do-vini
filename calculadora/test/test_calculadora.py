from django.test import TestCase
from calculadora import views


class CalculadoraTest(TestCase):
    def test_soma(self):
        self.assertEqual(views.soma(2, 2), 4)

    def test_mult(self):
        self.assertEqual(views.mult(4, 4), 16)

    def test_divisao(self):
        self.assertEqual(views.divisao(3, 3), 1)

    def test_sub(self):
        self.assertEqual(views.sub(10, 5), 5)


