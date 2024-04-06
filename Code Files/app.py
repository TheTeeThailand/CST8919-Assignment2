from flask import Flask, request, redirect, session, render_template
from requests_oauthlib import OAuth2Session
import os

app = Flask(__name__)

# Set up Google OAuth configuration
CLIENT_ID = '1059079526821-klf3nv61j1mqm5d8kit654lf1u8amlk5.apps.googleusercontent.com'
CLIENT_SECRET = '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'
REDIRECT_URI = 'https://127.0.0.1:5000/login/callback'
SCOPE = ['profile', 'email']
AUTHORIZATION_BASE_URL = 'https://accounts.google.com/o/oauth2/v2/auth'
TOKEN_URL = 'https://oauth2.googleapis.com/token'

# Secret key for session
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login')
def login():
    # Create an OAuth2Session instance
    google = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=SCOPE)
    # Generate authorization URL
    authorization_url, state = google.authorization_url(AUTHORIZATION_BASE_URL, access_type="offline")
    # Store OAuth state in session
    session['oauth_state'] = state
    # Redirect to Google's authorization URL to start authentication process
    return redirect(authorization_url)

@app.route('/login/callback')
def callback():
    # Ensure the 'state' parameter is present in the callback
    if 'state' not in request.args:
        return 'Error: State parameter missing'
    # Ensure the 'state' parameter matches the one stored in the session
    if request.args['state'] != session.get('oauth_state'):
        return 'Error: State mismatch'
    
    # Create OAuth2Session instance with client ID and redirect URI
    google = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, state=session['oauth_state'])
    # Fetch token using the authorization response
    token = google.fetch_token(TOKEN_URL, client_secret=CLIENT_SECRET, authorization_response=request.url)
    
    # At this point, you have the access token, you can use it to make requests to Google APIs
    # For example, you can get user info using the token like this:
    user_info = google.get('https://www.googleapis.com/oauth2/v3/userinfo').json()
    
    # Do something with the user info
    return "Authentication successful. User info: {}".format(user_info)

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')  # Enable SSL for HTTPS
