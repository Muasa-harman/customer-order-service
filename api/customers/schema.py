import graphene
from graphene_django import DjangoObjectType
from .models import Customer

class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = ("id", "name", "code", "phone")

class CreateCustomer(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        code = graphene.String(required=True)
        phone = graphene.String()

    customer = graphene.Field(CustomerType)

    @classmethod
    def mutate(cls, root, info, name, code, phone=None):
        customer = Customer(name=name, code=code, phone=phone)
        customer.save()
        return CreateCustomer(customer=customer)