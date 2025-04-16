from django.test import TestCase
from users.models import CustomUser
from customers.models import Customer

class UserModelTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpass123'))

class CustomerModelTest(TestCase):
    def test_customer_creation(self):
        user = CustomUser.objects.create_user(email='customer@example.com')
        customer = Customer.objects.create(
            user=user,
            code='CUST001'
        )
        self.assertEqual(customer.code, 'CUST001')