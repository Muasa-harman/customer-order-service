import graphene
from customers.graphql_schema import Query as CustomerQuery, CreateCustomer
from orders.graphql_schema import ConfirmOrder, Query as OrderQuery, CreateOrder



class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
    create_order = CreateOrder.Field()
    confirm_order = ConfirmOrder.Field()
#   class Mutation(graphene.ObjectType):
#     token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()
    

class Query(CustomerQuery, OrderQuery, graphene.ObjectType):
    pass



schema = graphene.Schema(query=Query, mutation=Mutation)