import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
import africastalking 

if not hasattr(africastalking, '_initialized'):
    africastalking.initialize(
        username='sandbox',
        api_key=os.getenv('AT_API_KEY')
    )
    africastalking._initialized = True

def send_sms(phone, message):
    try:
        sms = africastalking.SMS
        response = sms.send(message, [phone])
        print(f"SMS sent: {response}")

    except Exception as e:
        print(f"SMS failed:,{(e)}")
  
@receiver(post_save, sender=Order)
def order_created_handler(sender, instance, created, **kwargs):
    if instance.status == 'confirmed':
        message =( 
            f"Hi {instance.customer.name},"
            f"your order for {instance.item} (KES {instance.amount}) has been received!")
        send_sms(instance.customer.phone, message)