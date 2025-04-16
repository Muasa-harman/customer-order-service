import graphene
from graphene_django import DjangoObjectType
from graphql_jwt import ObtainJSONWebToken, Verify, Refresh
from users.models import CustomUser

class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'roles')

class AuthMutation(graphene.ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = Verify.Field()
    refresh_token = Refresh.Field()

class RegisterUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        roles = graphene.String(required=False)

    user = graphene.Field(UserType)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, email, password, roles=None):
        if CustomUser.objects.filter(email=email).exists():
            raise Exception("Email is already registered.")
        
        # Automatically generate a username from the email 
        username = email.split('@')[0]

        user = CustomUser.objects.create_user(email=email, password=password,username=username)
        
        if roles:
            user.roles = roles
        user.save()

        return RegisterUser(user=user, success=True, message="User registered successfully.")


class AuthQuery(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not authenticated!')
        return user   


class Mutation(AuthMutation, graphene.ObjectType):
    pass





# import graphene
# from graphene_django import DjangoObjectType
# from graphql_jwt import ObtainJSONWebToken, Verify, Refresh
# from users.models import CustomUser

# class UserType(DjangoObjectType):
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'email', 'roles')

# class AuthMutation(graphene.ObjectType):
#     token_auth = ObtainJSONWebToken.Field()
#     verify_token = Verify.Field()
#     refresh_token = Refresh.Field()

# class RegisterUser(graphene.Mutation):
#     class Arguments:
#         email = graphene.String(required=True)
#         password = graphene.String(required=True)
#         roles = graphene.String(required=False)
#         oidc_id = graphene.String(required=True)

#     user = graphene.Field(UserType)
#     success = graphene.Boolean()
#     message = graphene.String()

#     def mutate(self, info, email, password, roles=None,oidc_id=None):
#         if CustomUser.objects.filter(email=email).exists():
#             raise Exception("Email is already registered.")
        
#         # Automatically generate a username from the email 
#         username = email.split('@')[0]

#         if not oidc_id:
#             raise Exception("OIDC ID is required.")

#         user = CustomUser.objects.create_user(email=email, password=password,username=username,oidc_id=oidc_id)
        
#         if roles:
#             user.roles = roles
#         user.save()

#         return RegisterUser(user=user, success=True, message="User registered successfully.")


# class AuthQuery(graphene.ObjectType):
#     me = graphene.Field(UserType)

#     def resolve_me(self, info):
#         user = info.context.user
#         if user.is_anonymous:
#             raise Exception('Not authenticated!')
#         return user   


# class Mutation(AuthMutation, graphene.ObjectType):
#     pass