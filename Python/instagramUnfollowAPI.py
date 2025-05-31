# Note the most we can get fromr the server is 17 requests
from instagrapi import Client
from time import sleep
import webbrowser
import os
import getFollowing

# getFollowing.get_data()  # creates the files needed (this has been updated to return)

# Login to Instagram
username = "<USERNAME>"
password = "<PASSWORD>"
cl = Client()
cl.login(username, password)

file_path_non_follower = "C:\\Users\\david\\OneDrive\\Desktop\\InstagramCode\\non_follower.txt"
non_follower = list()
confirmed_unfollow = list()

def setup_non_follower():
    with open(file_path_non_follower, "r", encoding="utf-8") as file:
            content = file.read()
    
    non_follower1 = list(content.split('\n'))

    # remove all spaces
    for i in non_follower1:
            if i != "":
                non_follower.append(i)

def show_unfollow_user(username):
    url = f"https://www.instagram.com/{username}/"
    webbrowser.open(url)

def unfollow():
    # unfollow people
    unfollow_exception = {"loyolamaryland","opeyemifamakin","loyolamesa","this.isnt_momo","joychristheaven","kinematronics","soulx_quote_","soulxsigh","jude.oc","victorianpoetry","networkchuck", "brainjotter","troyhawke","_dailycoding","anwar"}
    tracker = 1
    for user in non_follower:
        if user not in unfollow_exception:
            try:
                user_id = cl.user_id_from_username(user)
                print(f"Unfollowing user: {user}")   # safe mode
                sleep(3)
                print(2)
                sleep(3)
                print(1)
                cl.user_unfollow(user_id)
                
                non_follower.remove(user)  # remove from the list
                user += '\n'
                confirmed_unfollow.append(user)  # add to the confirmed list
                
                if tracker == 100:
                    break
                tracker += 1
            except:
                with open("C:\\Users\\david\\OneDrive\\Desktop\\InstagramCode\\confirmed_unfollow.txt","a") as file:
                    file.writelines(item + '\n' for item in confirmed_unfollow)

                with open("C:\\Users\\david\\OneDrive\\Desktop\\InstagramCode\\non_follower.txt","w") as file:
                    file.writelines(item + '\n' for item in non_follower)
                return
    with open("C:\\Users\\david\\OneDrive\\Desktop\\InstagramCode\\confirmed_unfollow.txt","a") as file:
        file.writelines(item + '\n' for item in confirmed_unfollow)
    with open("C:\\Users\\david\\OneDrive\\Desktop\\InstagramCode\\non_follower.txt","w") as file:
        file.writelines(item + '\n' for item in non_follower)

setup_non_follower()
unfollow()

