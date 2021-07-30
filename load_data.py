import pandas as pd
import get_usernames

def _get_tweets(username, raw=True):
    str_path = "raw"
    if not raw: str_path = "clean"
    
    path = f"data/tweets-{str_path}-{username}.csv"
    return pd.read_csv(path, engine='python', error_bad_lines=False)

def get_tweets(username):
    return _get_tweets(username, raw=True)

def get_clean_tweets(username):
    return _get_tweets(username, raw=False)

def save_cleaned_tweets(tweets_df, username):
    tweets_df.to_csv(f"data/tweets-clean-{username}.csv", index=False)
    
def get_all_tweets():
    tweets_all = []
    usernames = get_usernames.get_usernames()
    
    for username in usernames:
        tweets = get_tweets(username)
        tweets_all.append(tweets)
    
    return tweets_all

def get_all_clean_tweets():
    tweets_all = []
    usernames = get_usernames.get_usernames()
    
    for username in usernames:
        tweets = get_clean_tweets(username)
        tweets_all.append(tweets)
    
    return tweets_all


def get_all_tweets_dict():
    tweets_all = {}
    usernames = get_usernames.get_usernames()
    
    for username in usernames:
        tweets = get_tweets(username)
        tweets_all[username] = (tweets)
    
    return tweets_all

def get_all_clean_tweets_dict():
    tweets_all = {}
    usernames = get_usernames.get_usernames()
    
    for username in usernames:
        tweets = get_clean_tweets(username)
        tweets_all[username] = (tweets)
    
    return tweets_all