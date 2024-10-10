# Twitter API Interaction Assignment

## Introduction
This assignment detailed how to interact with the Twitter API by creating and deleting tweets using a Python program.The project helps  understand how to work with external APIs, use OAuth authentication, and manage API responses. from this assignment how to perform tasks such as posting a tweet and deleting a tweet programmatically while handling errors and rate limiting.

By completing this assignment,
- Learn how to authenticate with the Twitter API using OAuth.
- Gain experience making POST requests to create a new tweet.
- Understand how to make DELETE requests to remove an existing tweet.
- Practice writing well-documented code.
  
## Setup Instructions

### 1. Set Up a Twitter Developer Account
Before interact with the Twitter API, need to create a developer account and generate API keys:
- Create a [Twitter Developer Account](https://developer.twitter.com/).
- Once  account is approved, create a new project and an app under your Twitter Developer Dashboard.
- I use the defaut project.
  
### 2. Generate API Keys
Follow these steps to generate the necessary API keys:
1. Navigate to **Projects & Apps** → **Your App** → **Keys and Tokens**.
2. Generate the following credentials:
   - **API Key** (Consumer Key)
   - **API Secret Key** (Consumer Secret)
   - **Bearer Token**
   - **Access Token**
   - **Access Token Secret**

Make sure to store these credentials securely this  will need  in the program.

### 3. Configure OAuth
- Set the **Callback URL** to `http://localhost:3000` (or any local testing environment).
- Enable **User Authentication Settings** under the App settings to allow you to interact with your Twitter account.

## Program Details

### Posting a New Tweet
The program uses Tweepy, a Python library for accessing the Twitter API, to post a tweet. The function `post_tweet` handles this functionality by sending a POST request to the **statuses/update** endpoint.

### To run the program 
To run program Add  Twitter API credentials (API Key, API Secret Key, Access Token, and Access Token Secret) to the Python script and run python script.

python demo.py

![image](https://github.com/user-attachments/assets/a43560c2-15b5-4766-b31a-5db32f0b0a31)

In the twitter account you can see the post as shown in the below

![image](https://github.com/user-attachments/assets/07907177-112b-4c2b-a464-eb4916a2bdf5)


### Deleting an existing Account 
To delete an existing tweet, the program uses the POST statuses/destroy/:id endpoint. For deleting required to give the tweet ID .
Run the below to delete existing Account 

Python delete.py

![image](https://github.com/user-attachments/assets/edf88f14-5ec9-4ee8-86f6-2a72e031fc89)

In the twitter account you can see the post is deleted as shown in the below

![image](https://github.com/user-attachments/assets/02b0b174-cedf-4c17-947b-7ce8a8cabeb7)

### API Response 
Posting a Tweet: A JSON response with details of the newly created tweet  
Deleting a Tweet: A JSON response confirming the deletion of the tweet.

### Error handling 
The program includes error handling to manage various issues that may arise when interacting with the Twitter API, such as:

- Invalid credentials: The program checks if your API keys and tokens are correct.
- Rate limiting: Twitter has rate limits for API requests. If you exceed these limits, the program will catch the error and handle it gracefully.
- Invalid tweet ID: When deleting a tweet, the program ensures that a valid tweet ID is provided. If an invalid ID is used, the program catches the error and prints an appropriate message.

Below shows the Error handling sceenshot 

<img width="958" alt="image" src="https://github.com/user-attachments/assets/228af9e9-a8a9-4cf0-9e6b-502c6ad9d252">


