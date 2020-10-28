from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()

# django-oauth-toolkit
# https://django-oauth-toolkit.readthedocs.io/en/latest/getting_started.html
# https://www.django-rest-framework.org/api-guide/authentication/#django-oauth-toolkit
# https://www.liip.ch/en/blog/authorization-code-with-pkce-on-django-using-django-oauth-toolkit

def authorization_code_flow():
    # https://codeloop.org/django-social-login-authentication-example/

    # https://docs.authlib.org/en/stable/client/oauth2.html
    # https://www.oauth.com/oauth2-servers/server-side-apps/example-flow/
    # https://docs.github.com/en/free-pro-team@latest/developers/apps/scopes-for-oauth-apps
    # https://www.youtube.com/watch?v=m5sHDaBwxjc

    client_id = '061cc79cf9983a3b71c6'
    client_secret = '1b15d05e0f440d393f5b9e78953b45479bdaee93'
    scope = 'user:email'  # we want to fetch user's email
    # scope = 'user public_repo'

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
    # https://github.com/login/oauth/authorize?response_type=code&client_id=061cc79cf9983a3b71c6&scope=user+public_repo&state=byalzWy9PjL6tPNRc1YSC3HPicDqYt

    # if cancel 
    # https://www.google.com/?error=access_denied&error_description=The+user+has+denied+your+application+access.&error_uri=https%3A%2F%2Fdocs.github.com%2Fapps%2Fmanaging-oauth-apps%2Ftroubleshooting-authorization-request-errors%2F%23access-denied&state=jwOA06wTrrMXRBXpwy8iRYD1Yuasrt

    # after that just copy above uri and paste it in browser,u will get bellow  authorization_response url

    # authorization_response = 'https://www.google.com/?code=c1fcd5445035d9c1152e&state=pojk9RyDmfLHljJPYEiZd8JBCOkFZd'
    authorization_response='https://www.google.com/?code=b281d6b3129ac7125345&state=byalzWy9PjL6tPNRc1YSC3HPicDqYt'
    token_endpoint = 'https://github.com/login/oauth/access_token'
    # token = client.fetch_token(token_endpoint, authorization_response=authorization_response)
    # token={'access_token': 'd0b99754172aee541bb3fedb409f5759692900e8', 'token_type': 'bearer', 'scope': 'user:email'}
    token={'access_token': '04014f6f1cfe33c958b728d96f977c7b42bcca53', 'token_type': 'bearer', 'scope': 'public_repo,user'}
    print(token)

    client = OAuth2Session(client_id, client_secret, token=token)
    account_url = 'https://api.github.com/user'
    resp = client.get(account_url)      
    pprint(resp.json(),indent=4)

# authorization_code_flow()

# GitHub doesn’t support token response type, try with other services.
def implicit_flow():

    client_id = '061cc79cf9983a3b71c6'
    client_secret = '1b15d05e0f440d393f5b9e78953b45479bdaee93'
    scope = 'user:email'  # we want to fetch user's email
    # scope = 'user public_repo'

    # using requests implementation
    from authlib.integrations.requests_client import OAuth2Session
    client = OAuth2Session(client_id, client_secret, scope=scope)

    authorization_endpoint = 'https://github.com/login/oauth/authorize'
    uri, state = client.create_authorization_url(authorization_endpoint, response_type='token')
    print(uri)
    # https://github.com/login/oauth/authorize?response_type=token&client_id=061cc79cf9983a3b71c6&scope=user%3Aemail&state=IQZgbyQTRP9l2TugkDJbl2sJCLTyqp

    authorization_response="https://www.google.com/?code=099cabb70948a197bd5d&state=IQZgbyQTRP9l2TugkDJbl2sJCLTyqp"
    token = client.fetch_token(authorization_response=authorization_response)
    # # if you don't specify access token endpoint, it will fetch from fragment.
    # print(token)

# implicit_flow()


def OAuth2Session_for_Password_flow():

    client_id = '061cc79cf9983a3b71c6'
    client_secret = '1b15d05e0f440d393f5b9e78953b45479bdaee93'
    scope = 'user:email'  # we want to fetch user's email
    # scope = 'user public_repo'

    # using requests implementation
    from authlib.integrations.requests_client import OAuth2Session
    client = OAuth2Session(client_id, client_secret, scope=scope)

    
    token_endpoint = 'https://github.com/oauth/token'
    username=os.getenv('GITHUB_USERNAME')   
    password=os.getenv('GITHUB_PASSWORD')   
    print(username,'-->username',token_endpoint)
    credentials={'username':username ,'password':password}
    token = client.fetch_token(token_endpoint,username=username,password=password,grant_type='password')
    print(token)     

OAuth2Session_for_Password_flow()


def OAuth2Session_for_Client_Credentials():

    client_id = '061cc79cf9983a3b71c6'
    client_secret = '1b15d05e0f440d393f5b9e78953b45479bdaee93'
    scope = 'user:email'  # we want to fetch user's email
    # scope = 'user public_repo'

    # using requests implementation
    from authlib.integrations.requests_client import OAuth2Session
    client = OAuth2Session(client_id, client_secret, scope=scope)


    token_endpoint = 'https://github.com/login/oauth/access_token'
  
    token = client.fetch_token(token_endpoint,grant_type='client_credentials')

# OAuth2Session_for_Client_Credentials()