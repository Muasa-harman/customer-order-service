from graphene.test import Client
from django.test import TestCase
from api.schema import schema
from orders.models import Order  # adjust to your app name
from customers.models import Customer

class GraphQLTest(TestCase):
    def setUp(self):
    # Create a test customer
        self.customer = Customer.objects.create(
            name="Test Customer",
            code="CUST001",
            phone="+1234567890"
        )

    def test_create_order(self):
        client = Client(schema)
        query = '''
            mutation {
                createOrder(input: {
                    customerCode: "CUST001",
                    item: "Laptop",
                    quantity: 1,
                    unitPrice: 1000
                }) {
                    order {
                        id
                        amount
                    }
                }
            }
        '''
        result = client.execute(query)

        print(result)
        
        self.assertIsNone(result.get('errors'))
        order_data = result['data']['createOrder']['order']
        self.assertIsNone(result.get('errors'))
        self.assertEqual(order_data['amount'], 1000)
        self.assertGreater(result['data']['createOrder']['order']['amount'], 0)