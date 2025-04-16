from graphene.test import Client
from django.test import TestCase
from api.schema import schema

class GraphQLTest(TestCase):
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
        self.assertIsNone(result.get('errors'))
        self.assertGreater(result['data']['createOrder']['order']['amount'], 0)