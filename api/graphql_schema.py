import graphene
from customers.graphql_schema import Query as CustomerQuery, Mutation as CustomerMutation
from orders.graphql_schema import Query as OrderQuery , Mutation as OrderMutation



class Query(CustomerQuery, OrderQuery, graphene.ObjectType):
    pass

class Mutation(CustomerMutation, OrderMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)