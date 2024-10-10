import tweepy

# Set up Twitter API credentials
consumer_key = 'Ii1ZRzDk2r1u8SCEoeFvtBZb5'  # API Key
consumer_secret = 't39Q0Nh4dZiG3QsbKYe0D56rLutGqC3X0iYhywI3LvZKbDS8A4'  # API Key Secret
access_token = '1844361366070505482-Datzvvo16RMBpHQgaUT4haZChotqfA'  # Access Token
access_token_secret = 'i7U4lwEuj1etD8jZcX83qAEqQKBbZ2El18sDfKM5Lhm7k'  # Access Token Secret

# Authenticate to Twitter using OAuth1
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)

# Create the Tweepy API object
api = tweepy.API(auth)

# Function to delete a tweet
def delete_tweet():
    while True:
        try:
            # Get user input for the Tweet ID
            tweet_id = input("Enter the Tweet ID you want to delete (or type 'exit' to quit): ")

            # Exit condition
            if tweet_id.lower() == 'exit':
                print("Exiting the program.")
                break

            # Check for empty Tweet ID
            if not tweet_id.strip():
                print("Tweet ID cannot be empty. Please try again.")
                continue

            # Delete the tweet
            api.destroy_status(tweet_id)
            print(f"Tweet with ID {tweet_id} deleted successfully!")

        except tweepy.errors.NotFound:
            print(f"Tweet with ID {tweet_id} not found. Please verify the Tweet ID.")
        except tweepy.errors.Forbidden as e:
            print(f"Forbidden: You don't have permission to delete this tweet. {e}")
        except tweepy.errors.TooManyRequests:
            print("Rate limit exceeded. Please wait and try again later.")
        except tweepy.TweepyException as e:
            # Handle any other errors during the deletion process
            print(f"Failed to delete tweet: {e}")
        except Exception as e:
            # Catch any other unexpected exceptions
            print(f"An unexpected error occurred: {e}")

# Run the tweet deletion function
if __name__ == "__main__":
    delete_tweet()
