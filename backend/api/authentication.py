from django.contrib.auth.models import User
from rest_framework import authentication
from .exceptions import InvalidAuthToken
import firebase_admin.auth as auth


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        token = request.headers.get('Authorization').split(" ").pop()
        if not token:
            return None

        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token["uid"]
        except Exception:
            raise InvalidAuthToken("Invalid auth token")
            
        user, created = User.objects.get_or_create(username=uid)

        return (user, None)