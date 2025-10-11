import re

# Make sure to have these two files active; in the correct path
#To fill in the data: get the html . font from the exported instagram data
file_path_follower = "files\\follower.txt"
file_path_following = "files\\following.txt"

following = list()
follower = list()
non_follower = list()

def extract_words(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Regular expression to find text between ">" and "<"
    matches = re.findall(r'>(.*?)<', content)

    return list(matches)

following_temp = extract_words(file_path_following)
follower_temp = extract_words(file_path_follower)
month_abb = {"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"}

def get_following():

    print("--List of People I Follow--")

    for user_temp in following_temp:
        three_first = user_temp[:3]
        if three_first not in month_abb and not user_temp.startswith("http"): #check for error
            user_temp += '\n'
            following.append(user_temp)
    print(f"Number of Following: {len(following)}")
    with open("files\\following_filtered.txt","w") as file:
        file.writelines(following)

def get_follower():

    print("--List of People Who Follow Me--")

    for user_temp in follower_temp:
        three_first = user_temp[:3]
        if three_first not in month_abb:
            user_temp += '\n'
            follower.append(user_temp)
    print(f"Number of Followers: {len(follower)}")        
    with open("files\\follower_filtered.txt","w") as file:
        file.writelines(follower)

def get_non_follower():

    print("--List of Non-Followers")

    for user in following:
        if user not in follower:
            user += '\n'
            non_follower.append(user)
    
    
    print(f"Number of EXPECTED non followers: {len(following)-len(follower)}")
    print(f"Number of THEORY non followers: {len(non_follower)}")
    with open("files\\non_follower.txt","w") as file:
        file.writelines(non_follower)
        

def get_data():
    get_follower()
    get_following()
    get_non_follower()
    print("D-o-n-e ---> Go into the path to confirm result!")
    return non_follower