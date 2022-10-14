from django.core.mail import send_mail
from real_state.settings.development import DEFAULT_FROM_EMAIL
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Enquiry

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def send_enquiry_email(request):
    data = request.data
    try:
        subject = data["subject"]
        name = data["name"]
        email = data["email"]
        message = data["message"]
        from_email = DEFAULT_FROM_EMAIL
        recipient_list = [data["email"]]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        enquiry = Enquiry(name=name, email=email, subject=subject, message=message)
        enquiry.save()

        return Response({"success": "Your Enquiry was successfully submitted"})

    except:
        return Response({"fail": "Enquiry was not sent"})