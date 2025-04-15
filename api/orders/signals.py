import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
import africastalking # type: ignore

def send_sms_notification(customer_phone, message):
    # Initialize sandbox
    africastalking.initialize(
        username='sandbox', 
        api_key=os.getenv('AT_API_KEY')
    )
    sms = africastalking.SMS
    sms.send(message, [customer_phone])

@receiver(post_save, sender=Order)
def order_created_handler(sender, instance, created, **kwargs):
    if created and instance.customer.phone:
        message = f"Hi {instance.customer.name}, your order for {instance.item} (KES {instance.amount}) has been received!"
        send_sms_notification(instance.customer.phone, message)