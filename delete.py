import tweepy

# Twitter API credentials (replace with your actual credentials)
API_KEY = 'Ii1ZRzDk2r1u8SCEoeFvtBZb5'
API_SECRET_KEY = 't39Q0Nh4dZiG3QsbKYe0D56rLutGqC3X0iYhywI3LvZKbDS8A4'
ACCESS_TOKEN = '1844361366070505482-Datzvvo16RMBpHQgaUT4haZChotqfA'
ACCESS_TOKEN_SECRET = 'i7U4lwEuj1etD8jZcX83qAEqQKBbZ2El18sDfKM5Lhm7k'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Function to delete a tweet by its ID
def delete_tweet(tweet_id):
    try:
        api.destroy_status(tweet_id)
        print(f"Tweet with ID {tweet_id} has been deleted.")
    except tweepy.TweepError as e:
        print(f"Failed to delete tweet: {e}")

# Replace 'tweet_id_here' with the actual tweet ID you want to delete
tweet_id = '1844372263581237537'
delete_tweet(tweet_id)
