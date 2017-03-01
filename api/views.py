import requests

from django.http import JsonResponse
from rest_framework import viewsets
from salesforce.models import Adopter
from salesforce.functions import check_if_faculty_pending, update_faculty_status, check_if_email_used
from social.apps.django_app.default.models import \
    DjangoStorage as SocialAuthStorage
from global_settings.models import StickyNote
from wagtail.wagtailimages.models import Image
from wagtail.wagtaildocs.models import Document

from .serializers import AdopterSerializer, ImageSerializer, DocumentSerializer


class AdopterViewSet(viewsets.ModelViewSet):
    queryset = Adopter.objects.all()
    serializer_class = AdopterSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def get_queryset(self):
        queryset = Document.objects.all()
        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = queryset.filter(title__icontains=search)
        return queryset


def user_api(request):
    user = request.user

    try:
        social_auth = SocialAuthStorage.user.get_social_auth_for_user(user)
        user.accounts_id = social_auth[0].uid
    except:
        user.accounts_id = None

    try:
        return JsonResponse({
            'id': user.pk,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
            'groups': list(user.groups.values_list('name', flat=True)),
            'accounts_id': user.accounts_id,
        })
    except:
        return JsonResponse({
            'id': False,
            'email': '',
            'username': '',
            'first_name': '',
            'last_name': '',
            'is_staff': False,
            'is_superuser': False,
            'groups': [],
            'accounts_id': None,
        })


def user_salesforce_update(request):
    print("sf update")

    r = requests.get('https://accounts-qa.openstax.org/api/user')

    user = request.user
    email = request.GET.get('email', None)
    salesforce_faculty_verified_failed = "Not Implemented"
    salesforce_verification_pending_failed = "Not Implemented"
    salesforce_email_previously_used = "Not Implemented"
    pending_verification = "Not Implemented"

    # get user account ID
    try:
        social_auth = SocialAuthStorage.user.get_social_auth_for_user(user)
        user.accounts_id = social_auth[0].uid
    except:
        user.accounts_id = None
    #
    # # check if user is faculty_verified in SF
    # try:
    #     verification_status = update_faculty_status(user.pk)
    # except:
    #     salesforce_faculty_verified_failed = True
    #
    # # check if there is a record in SF for this user - if so, they are pending verification
    # try:
    #     pending_verification = check_if_faculty_pending(user.pk)
    #     if email:
    #         salesforce_email_previously_used  = check_if_email_used(email)
    #
    # except Exception as err:
    #     print(err)
    #     pending_verification = str(err)
    #     salesforce_email_previously_used = str(err)

    if user.is_authenticated():
        return JsonResponse({
                'username': user.username,
                'status_code': r.status_code,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser,
                'groups': list(user.groups.values_list('name', flat=True)),
                'accounts_id': user.accounts_id,
                'pending_verification': pending_verification,
                'salesforce_faculty_verified_failed': salesforce_faculty_verified_failed,
                'salesforce_verification_pending_failed': salesforce_verification_pending_failed,
                'salesforce_email_previously_used': salesforce_email_previously_used,
            })
    else:
        return JsonResponse({})


def sticky_note(request):
    sticky_note = StickyNote.for_site(request.site)

    return JsonResponse({
        'show': sticky_note.show,
        'expires': sticky_note.expires,
        'content': sticky_note.content,
        'emergency_expires': sticky_note.emergency_expires,
        'emergency_content': sticky_note.emergency_content,
    })
