"""
Auth2 -> 1st implementation
authorization_code_flow



def authorization_code_flow():
    # https://codeloop.org/django-social-login-authentication-example/

    # https://docs.authlib.org/en/stable/client/oauth2.html
    # https://www.oauth.com/oauth2-servers/server-side-apps/example-flow/
    # https://docs.github.com/en/free-pro-team@latest/developers/apps/scopes-for-oauth-apps

    client_id = '1883b0b8014c6c2a6bec'
    client_secret = '992f5a5e29c5a708c6d7179f5aa07789a5c2a57d'
    # scope = 'user:email'  # we want to fetch user's email
    scope = 'user public_repo'
    # using requests implementation
    from authlib.integrations.requests_client import OAuth2Session
    client = OAuth2Session(client_id, client_secret, scope=scope)
    # print(dir(client),client.token_auth,'--->see')
    # using httpx implementation
    # from authlib.integrations.httpx_client import AsyncOAuth2Client
    # client = AsyncOAuth2Client(client_id, client_secret, scope=scope)

    # Unlike OAuth 1, there is no request token. The first step is to jump to the remote authorization server:

    # The create_authorization_url returns a tuple of (uri, state), in real project, you should save the state for later use.
    authorization_endpoint = 'https://github.com/login/oauth/authorize'
    uri, state = client.create_authorization_url(authorization_endpoint)
    print(uri,'-->uri')
    # https://github.com/login/oauth/authorize?response_type=code&client_id=1883b0b8014c6c2a6bec&scope=user+public_repo&state=jwOA06wTrrMXRBXpwy8iRYD1Yuasrt

    # if cancel 
    # https://www.google.com/?error=access_denied&error_description=The+user+has+denied+your+application+access.&error_uri=https%3A%2F%2Fdocs.github.com%2Fapps%2Fmanaging-oauth-apps%2Ftroubleshooting-authorization-request-errors%2F%23access-denied&state=jwOA06wTrrMXRBXpwy8iRYD1Yuasrt
    # after that just copy above uri and paste it in browser,u will get bellow  authorization_response url

    # authorization_response = 'https://www.google.com/?code=c1fcd5445035d9c1152e&state=pojk9RyDmfLHljJPYEiZd8JBCOkFZd'
    authorization_response='https://www.google.com/?code=6dded4bb6029f1b41d15&state=jwOA06wTrrMXRBXpwy8iRYD1Yuasrt'
    token_endpoint = 'https://github.com/login/oauth/access_token'
    token = client.fetch_token(token_endpoint, authorization_response=authorization_response)
    # token={'access_token': 'd0b99754172aee541bb3fedb409f5759692900e8', 'token_type': 'bearer', 'scope': 'user:email'}
    token={'access_token': '5b23b0db5983b3f174a884fc4a6e4f51ad482468', 'token_type': 'bearer', 'scope': 'public_repo,user'}
    print(token)

    # {'access_token': 'd0b99754172aee541bb3fedb409f5759692900e8', 'token_type': 'bearer', 'scope': 'user:email'}


    # token = restore_previous_token_from_database()
    client = OAuth2Session(client_id, client_secret, token=token)
    account_url = 'https://api.github.com/user'
    resp = client.get(account_url)      
    pprint(resp.json(),indent=4)

authorization_code_flow()



https://github.com/login/oauth/authorize?response_type=code&client_id=1883b0b8014c6c2a6bec&scope=user+public_repo&state=jwOA06wTrrMXRBXpwy8iRYD1Yuasrt -->uri
d0b99754172aee541bb3fedb409f5759692900e8
{   'avatar_url': 'https://avatars1.githubusercontent.com/u/44753622?v=4',
    'bio': None,
    'blog': '',
    'company': None,
    'created_at': '2018-11-04T18:41:20Z',
    'email': None,
    'events_url': 'https://api.github.com/users/Saurabh323351/events{/privacy}',
    'followers': 3,
    'followers_url': 'https://api.github.com/users/Saurabh323351/followers',
    'following': 22,
    'following_url': 'https://api.github.com/users/Saurabh323351/following{/other_user}',
    'gists_url': 'https://api.github.com/users/Saurabh323351/gists{/gist_id}',
    'gravatar_id': '',
    'hireable': None,
    'html_url': 'https://github.com/Saurabh323351',
    'id': 44753622,
    'location': None,
    'login': 'Saurabh323351',
    'name': 'Saurabh Singh',
    'node_id': 'MDQ6VXNlcjQ0NzUzNjIy',
    'organizations_url': 'https://api.github.com/users/Saurabh323351/orgs',
(Python-OAUTH2) ➜  Python-OAUTH2 python python-oauth2.py
https://github.com/login/oauth/authorize?response_type=code&client_id=1883b0b8014c6c2a6bec&scope=user+public_repo&state=Tq6I4WWEhY9kiXntoZDJiiUoxzZPPI -->uri
Traceback (most recent call last):
  File "/home/saurabh/Videos/Python-OAUTH2/python-oauth2.py", line 47, in <module>
    r=first()
  File "/home/saurabh/Videos/Python-OAUTH2/python-oauth2.py", line 33, in first
    token = client.fetch_token(token_endpoint, authorization_response=authorization_response)
  File "/home/saurabh/.local/share/virtualenvs/Python-OAUTH2-TY9aSrrj/lib/python3.9/site-packages/authlib/oauth2/client.py", line 203, in fet
(Python-OAUTH2) ➜  Python-OAUTH2 python python-oauth2.py
https://github.com/login/oauth/authorize?response_type=code&client_id=1883b0b8014c6c2a6bec&scope=user+public_repo&state=eqRE7HUL7n1ua19p6CrGz3wKkcdDkX -->uri
{'access_token': '5b23b0db5983b3f174a884fc4a6e4f51ad482468', 'token_type': 'bearer', 'scope': 'public_repo,user'}
{   'avatar_url': 'https://avatars1.githubusercontent.com/u/44753622?v=4',
    'bio': None,
    'blog': '',
    'collaborators': 0,
    'company': None,
    'created_at': '2018-11-04T18:41:20Z',
    'disk_usage': 367526,
    'email': None,
    'events_url': 'https://api.github.com/users/Saurabh323351/events{/privacy}',
    'followers': 3,
    'followers_url': 'https://api.github.com/users/Saurabh323351/followers',
    'following': 22,
    'following_url': 'https://api.github.com/users/Saurabh323351/following{/other_user}',
    'gists_url': 'https://api.github.com/users/Saurabh323351/gists{/gist_id}',
    'gravatar_id': '',
    'hireable': None,
    'html_url': 'https://github.com/Saurabh323351',
    'id': 44753622,
    'location': None,
    'login': 'Saurabh323351',
    'name': 'Saurabh Singh',
    'node_id': 'MDQ6VXNlcjQ0NzUzNjIy',
    'organizations_url': 'https://api.github.com/users/Saurabh323351/orgs',
    'owned_private_repos': 16,
    'plan': {   'collaborators': 0,
                'name': 'free',
                'private_repos': 10000,
                'space': 976562499},
    'private_gists': 1,
    'public_gists': 0,
    'public_repos': 31,
    'received_events_url': 'https://api.github.com/users/Saurabh323351/received_events',
    'repos_url': 'https://api.github.com/users/Saurabh323351/repos',
    'site_admin': False,
    'starred_url': 'https://api.github.com/users/Saurabh323351/starred{/owner}{/repo}',
    'subscriptions_url': 'https://api.github.com/users/Saurabh323351/subscriptions',
    'total_private_repos': 16,
    'twitter_username': None,
    'two_factor_authentication': False,
    'type': 'User',
    'updated_at': '2020-10-27T10:50:37Z',
    'url': 'https://api.github.com/users/Saurabh323351'}



#Bridgelabz Id github data saurabh.singh@bridgelabz.com 

https://github.com/login/oauth/authorize?response_type=code&client_id=061cc79cf9983a3b71c6&scope=user%3Aemail&state=QqXgLlVL7qCpfX4KpM9cJnxnV35uEq -->uri
{'access_token': '04014f6f1cfe33c958b728d96f977c7b42bcca53', 'token_type': 'bearer', 'scope': 'public_repo,user'}
{   'avatar_url': 'https://avatars0.githubusercontent.com/u/66241210?v=4',
    'bio': None,
    'blog': '',
    'collaborators': 0,
    'company': None,
    'created_at': '2020-06-01T06:50:35Z',
    'disk_usage': 8,
    'email': 'saurabh.singh@bridgelabz.com',
    'events_url': 'https://api.github.com/users/saurabh-bridgelabz/events{/privacy}',
    'followers': 0,
    'followers_url': 'https://api.github.com/users/saurabh-bridgelabz/followers',
    'following': 0,
    'following_url': 'https://api.github.com/users/saurabh-bridgelabz/following{/other_user}',
    'gists_url': 'https://api.github.com/users/saurabh-bridgelabz/gists{/gist_id}',
    'gravatar_id': '',
    'hireable': None,
    'html_url': 'https://github.com/saurabh-bridgelabz',
    'id': 66241210,
    'location': None,
    'login': 'saurabh-bridgelabz',
    'name': 'Saurabh',
    'node_id': 'MDQ6VXNlcjY2MjQxMjEw',
    'organizations_url': 'https://api.github.com/users/saurabh-bridgelabz/orgs',
    'owned_private_repos': 1,
    'plan': {   'collaborators': 0,
                'name': 'free',
                'private_repos': 10000,
                'space': 976562499},
    'private_gists': 0,
    'public_gists': 0,
    'public_repos': 2,
    'received_events_url': 'https://api.github.com/users/saurabh-bridgelabz/received_events',
    'repos_url': 'https://api.github.com/users/saurabh-bridgelabz/repos',
    'site_admin': False,
    'starred_url': 'https://api.github.com/users/saurabh-bridgelabz/starred{/owner}{/repo}',
    'subscriptions_url': 'https://api.github.com/users/saurabh-bridgelabz/subscriptions',
    'total_private_repos': 1,
    'twitter_username': None,
    'two_factor_authentication': False,
    'type': 'User',
    'updated_at': '2020-10-27T14:02:48Z',
    'url': 'https://api.github.com/users/saurabh-bridgelabz'}


"""












































"""
settings.py

Django settings for fundooapp project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k8b^y952f(10ox6993@h0q3-+&d_r#-g!qu+1zpggva_kux)2x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',

    'users',
    'fundoonotes',

    'django_nose'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware'
]

#
# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
# ]

ROOT_URLCONF = 'fundooapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'fundooapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'fundoonotes',
        'USER': 'fundoouser',
        'PASSWORD': 'fundoouser',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=users,fundooNotes',
]

"""
