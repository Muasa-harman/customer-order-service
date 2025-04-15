import graphene
from graphene_django import DjangoObjectType
from django.core.exceptions import ValidationError
from .models import Order
from customers.models import Customer

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = ("id", "customer", "item", "amount", "time")

class OrderInput(graphene.InputObjectType):
    customer_code = graphene.String(required=True)
    item = graphene.String(required=True)
    amount = graphene.Decimal(required=True)
        

class Query(graphene.ObjectType):
    all_orders = graphene.List(OrderType)
    orders_by_customer = graphene.List(OrderType, customer_code=graphene.String(required=True))

    def resolve_all_orders(self, info):
        return Order.objects.all()

    def resolve_orders_by_customer(self, info, customer_code):
        customer = Customer.objects.get(code=customer_code)
        return Order.objects.filter(customer=customer)

class CreateOrder(graphene.Mutation):
    class Arguments:
        input = OrderInput(required=True)

    order = graphene.Field(OrderType)
    success = graphene.Boolean()
    message = graphene.String()
    errors = graphene.List(graphene.String)

    def mutate(self, info,input):
        try:
            if not input.item.strip():
                raise ValidationError("Item cannot be empty.")
            
            if input.amount <= 0:
                raise ValidationError("Amount must be greater than 0.")
            
            customer = Customer.objects.get(code=input.customer_code)

            # validate order
            order = Order(customer=customer, item=input.item, amount=input.amount)
            order.full_clean()
            order.save()

            return CreateOrder(order=order,success=True,message="Order created successfully!",errors=[])
        except Customer.DoesNotExist:
            return CreateOrder(
                order = None,
                success=False,
                message="Validattion failed.",
                errors=["Customer does not exist."]
            )
        except ValidationError as e:
            return CreateOrder(
                order=None,
                success=False,
                message="Validation failed.",
                errors=e.message
            )

class Mutation(graphene.ObjectType):
    create_order = CreateOrder.Field()