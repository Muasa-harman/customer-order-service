import graphene
from customer_order_service.customers.models import Customer
from customer_order_service.orders.models import Order
from customers.schema import CustomerType, CreateCustomer
from orders.schema import OrderType, CreateOrder

class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)
    all_orders = graphene.List(OrderType)

    def resolve_all_customers(root, info):
        return Customer.objects.all()

    def resolve_all_orders(root, info):
        return Order.objects.all()

class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
    create_order = CreateOrder.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)