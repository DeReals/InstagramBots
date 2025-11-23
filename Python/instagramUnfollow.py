#important note: When you export the data follow this step in microsoft edgr
#  1. GO TO INSPECT
#  2. GO TO SOURCE
#  3. COPY THE CONTENT IN "".HTML

# Note the most we can get fromr the server is 17 requests
from time import sleep
import webbrowser
import os
import getFollowing

non_follower = getFollowing.get_data()  # this should setup the files

def unfollow(username):
    if("/" in username):
        url = username
    else:
        url = f"https://www.instagram.com/{username}/"
    webbrowser.open(url)
    sleep(2)
    #os.system("taskkill /F /IM msedge.exe")  # for windows

# setup_non_follower
non_follower = [word.strip() for word in non_follower]

error_list = list()

for user in non_follower:
    if " " not in user:
        unfollow(user)
        #print(user)
    else:
        error_list.append(user)

print(error_list)

print("Done")