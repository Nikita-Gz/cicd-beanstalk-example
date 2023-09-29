from django.test import TestCase


class ExampleTest(TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(1, 2 - 1)

    def test2(self):
        self.assertEqual(1 + 2, 2 + 1)
