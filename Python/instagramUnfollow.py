# Note the most we can get fromr the server is 17 requests
from time import sleep
import webbrowser
import os
import getFollowing

non_follower = getFollowing.get_data()  # this should setup the files

def unfollow(username):
    url = f"https://www.instagram.com/{username}/"
    webbrowser.open(url)
    sleep(10)
    os.system("taskkill /F /IM msedge.exe")  # for windows

# setup_non_follower
non_follower = [word.strip() for word in non_follower]

error_list = list()

for user in non_follower:
    if " " not in user:
        unfollow(user)
    else:
        error_list.append(user)

print(error_list)