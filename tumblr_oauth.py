
from requests_oauthlib import OAuth1Session

# Your Tumblr app credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
oauth_token = 'YOUR_OAUTH_TOKEN'
oauth_token_secret = 'YOUR_OAUTH_TOKEN_SECRET'

# Initialize an OAuth1 session
tumblr = OAuth1Session(consumer_key,
                       client_secret=consumer_secret,
                       resource_owner_key=oauth_token,
                       resource_owner_secret=oauth_token_secret)

# Test the connection by making a request to a Tumblr endpoint
url = 'https://api.tumblr.com/v2/blog/deadsams.tumblr.com/posts'
response = tumblr.get(url)

# Output the response
if response.status_code == 200:
    print(response.json())
else:
    print("Failed to connect:", response.status_code)
