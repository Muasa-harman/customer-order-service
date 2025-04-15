
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

from api.customers import views 

urlpatterns = [
    path('create/', views.create_customer, name='create_customer'),
    path('<int:customer_id>/', views.customer_detail, name='customer_detail'),
]


