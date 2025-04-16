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
    

class AuthQuery(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not authenticated!')
        return user   


class Mutation(AuthMutation, graphene.ObjectType):
    pass