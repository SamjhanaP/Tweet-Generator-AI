def get_usernames():
    f = open("twitter_user_names.txt", "r")
    value = f.read()
    return value.splitlines()