import graphene
from users.graphql_schema import AuthMutation, AuthQuery, RegisterUser
from customers.graphql_schema import Query as CustomerQuery, CreateCustomer
from orders.graphql_schema import ConfirmOrder, Query as OrderQuery, CreateOrder



class Mutation(AuthMutation, graphene.ObjectType):
    register_user = RegisterUser.Field()
    # token_auth, verify_token, refresh_token are already included via AuthMutation
    
    # Customer mutations
    create_customer = CreateCustomer.Field()
    create_order = CreateOrder.Field()
    confirm_order = ConfirmOrder.Field()
#   class Mutation(graphene.ObjectType):
#     token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()
    

class Query(CustomerQuery, OrderQuery,AuthQuery, graphene.ObjectType):
     # - Customers app
    # - Orders app
    # - Authentication app (e.g., me query)
    pass



schema = graphene.Schema(query=Query, mutation=Mutation)