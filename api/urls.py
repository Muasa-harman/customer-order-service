
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .graphql_schema import schema




urlpatterns = [
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    # path('admin/', admin.site.urls),
]
