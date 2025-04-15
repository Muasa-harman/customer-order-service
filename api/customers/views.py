from django.http import HttpResponse

def create_customer(request):
    return HttpResponse("Customer created!")