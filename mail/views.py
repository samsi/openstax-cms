from django.shortcuts import redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.middleware import csrf

from rest_framework.decorators import api_view


@api_view(['POST', 'GET'])
def send_contact_message(request):
    if request.method == 'POST':
        to_address = request.POST.get("to_address", "").split(',')
        from_name = request.POST.get("from_name", "")
        from_address = request.POST.get("from_address", "")
        from_string = '{} <{}>'.format(from_name, from_address)
        subject = request.POST.get("subject", "")
        message_body = request.POST.get("message_body", "")

        send_mail(subject, message_body, from_string, to_address)

        return redirect('/contact-thank-you')
    # if this is not posting a message, let's send the csfr token back
    else:
        csrf_token = csrf.get_token(request)
        data = {'csrf_token': csrf_token}

        return JsonResponse(data)
