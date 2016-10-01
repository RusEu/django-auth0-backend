from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from your_project import settings as c
import requests

class Auth0Backend(authentication.BaseAuthentication):
    def authenticate(self, request):
        def get_user(token):
            try:
                user = self.get_user(token)
                return (user, None)
            except User.DoesNotExist:
                raise exceptions.AuthenticationFailed('No such user')
        token = request.META.get('HTTP_AUTH0_TOKEN')
        return get_user(token) if token else None

    def get_user(self,token):
        try:
            profile = self.get_profile(token)
            user = self.get_or_create_user(**profile)
            return user
        except Exception as e:
            raise exceptions.AuthenticationFailed(e)

    def get_profile(self,token):
        url = 'https://%s/userinfo?access_token=%s'
        user_url = url % (c.AUTH0_DOMAIN,token)

        user_info = requests.get(user_url)
        try :
            return user_info.json()
        except:
            raise exceptions.AuthenticationFailed(user_info.text)

    def get_or_create_user(self, **kwargs):
        username = kwargs.pop('user_id')
        if username:
            try:
                return User.objects.get(username__iexact=username)
            except User.DoesNotExist:
                email = kwargs.get('email', '')
                firstname = kwargs.get('family_name', '')
                lastname = kwargs.get('given_name', '')

                return User.objects.create(email=email,
                                        username=username,
                                        first_name=firstname,
                                        last_name=lastname)

        raise ValueError(_('Username or email can\'t be blank'))

