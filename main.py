import tweepy
import time

# Your Twitter API credentials
API_KEY = 'jJQ6srNAgh3dNFUutByA3d7zL'
API_KEY_SECRET = 'SbcY3oqsxFWPNb69xdJuT7hfXe60Mi7uZdlhP0OB4719RXNYhZ'
ACCESS_TOKEN = '1810007865354256384-XekdvB1egBQrpoGoAA5TEQSb18J23J'
ACCESS_TOKEN_SECRET = 'cJgRMc0Bwk4DHnYD9apBn2GQ4IQfXoxrwdxMycDa1j8G7'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAANC%2FuwEAAAAAtLNoAQYKxTKcb3doL6hYyfxkLLs%3DrmiO09qq3HtYGSuOylOanGf1oSX5XRSTugSiYjgEbZXk6FNCKO'

# Authenticate to the Twitter API
client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, consumer_secret=API_KEY_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

# Authenticate using Tweepy's OAuth1UserHandler
auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def upload_video(file_path):
    # Initialize the upload
    media = api.media_upload(filename=file_path, media_category='tweet_video')

    # Post the tweet with the uploaded video
    response = client.create_tweet(media_ids=[media.media_id], text='Monday Monkey Lives For The Weekend, Sir')
    print("Tweeted:", response.data)

# Run the upload_video function
video_path = 'mondays.mp4'  # Assuming the video file is named 'mondays.mp4'
upload_video(video_path)
