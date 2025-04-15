import graphene
from graphene_django import DjangoObjectType
from .models import Order
from customers.models import Customer

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = ("id", "customer", "item", "amount", "time")

class CreateOrder(graphene.Mutation):
    class Arguments:
        customer_code = graphene.String(required=True)
        item = graphene.String(required=True)
        amount = graphene.Decimal(required=True)

    order = graphene.Field(OrderType)

    @classmethod
    def mutate(cls, root, info, customer_code, item, amount):
        customer = Customer.objects.get(code=customer_code)
        order = Order(customer=customer, item=item, amount=amount)
        order.save()
        return CreateOrder(order=order)