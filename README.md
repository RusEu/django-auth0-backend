# django-auth0-backend
Django authentication backend for Auth0

##Configure

If you need it in Django:

<pre>
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', #Your by default django auth backend
    'django-app-where-you-store-the-new-backend.django-auth0-backend', #your new auth0 backend
)
</pre>

If you need it in Django Rest Framework

<pre>
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'django-app-where-you-store-the-new-backend.django-auth0-backend', #your new auth0 backend
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}
</pre>

in the django-auth0-backend you need to change the import config file with the file where you store your Auth0 domain.
Example:

**ADD IN** in your_app/settings.py:
> 
<pre>
AUTH0_DOMAIN = "your_app.eu.auth0.com"
</pre>
