import tweepy

# Twitter API v2 credentials
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAJ5WwQEAAAAANOBUPhlYhkImIU0zkfG3HgfVkCU%3DPbkM6WnEwrYBVwvB5CBhwScKP5nCRgbi35xtre0MUNgLJrxdjr',
                       consumer_key='Ii1ZRzDk2r1u8SCEoeFvtBZb5',
                       consumer_secret='t39Q0Nh4dZiG3QsbKYe0D56rLutGqC3X0iYhywI3LvZKbDS8A4',
                       access_token='1844361366070505482-Datzvvo16RMBpHQgaUT4haZChotqfA',
                       access_token_secret='i7U4lwEuj1etD8jZcX83qAEqQKBbZ2El18sDfKM5Lhm7k')

try:
    # Post a new tweet using Twitter API v2
    response = client.create_tweet(text="Hello from Twitter API v2!")
    print(f"Posted tweet ID: {response.data['id']}")
except tweepy.TweepError as e:
    print(f"Error occurred: {e}")
