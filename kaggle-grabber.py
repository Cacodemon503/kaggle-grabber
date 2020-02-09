#!/usr/bin/python3

import csv
import requests
from itertools import zip_longest

#--------------------------------------------MENU------------------------------------------------#

choice = input("Print [competitions], [datasets], [kernels], [discussion]: ")
page_limit_choice = input("""

Print [page] to setup page limit (GitHub checker will be activated). 
Print [get all] to get the full list of top-users (GitHub checker will be deactivated due to possible API requests limits): """)

#-----------------------------------GET ALL USERS MODE-------------------------------------------#

if page_limit_choice == "get all":
    print("Step: Collecting users, please wait ... ")

    page = 0
    users_nicknames_list = []
    users_fullnames_list = []
    users_points_list = []
    users_tier_list = []

    page = page + 1
    URL = "https://www.kaggle.com/rankings.json?group=" + str(choice) + "&page=" + str(page) + "&pageSize=20"
    r = requests.get(url = URL)
    headers = r.headers
    content = r.json()
        
    content_status = content["list"]
        
    users_nicknames = [i["userUrl"] for i in content["list"]]    
    users_nicknames_list.extend(users_nicknames)
    
    users_nicknames_list_noslash = [i[1:] for i in users_nicknames_list]
    
    users_fullnames = [i["displayName"] for i in content["list"]]
    users_fullnames_list.extend(users_fullnames)
    
    users_points = [i["points"] for i in content["list"]]
    users_points_list.extend(users_points)
    
    users_tier = [i["tier"] for i in content["list"]]
    users_tier_list.extend(users_tier)
    
    while content_status:
        page = page + 1
        URL = "https://www.kaggle.com/rankings.json?group=" + str(choice) + "&page=" + str(page) + "&pageSize=20"
        r = requests.get(url = URL)
        headers = r.headers
        content = r.json()
        
        content_status = content["list"]
        
        users_nicknames = [i["userUrl"] for i in content["list"]]
        
        users_nicknames_list.extend(users_nicknames)
        
        users_nicknames_list_noslash = [i[1:] for i in users_nicknames_list]
    
        users_fullnames = [i["displayName"] for i in content["list"]]
        users_fullnames_list.extend(users_fullnames)
    
        users_points = [i["points"] for i in content["list"]]
        users_points_list.extend(users_points)
    
        users_tier = [i["tier"] for i in content["list"]]
        users_tier_list.extend(users_tier)
        
        lists_all = list(zip_longest(users_nicknames_list_noslash, users_fullnames_list, users_points_list, users_tier_list))
        
    users_amount = len(users_nicknames_list_noslash)
    print("Collected: " + str(users_amount) + " users")

#---------------------------CSV WRITER [GET ALL USERS MODE]------------------------------------#    
    
    print("Step: Saving to CSV ...")
    with open("{}.txt".format(str(input("Enter file name: "))), "w", encoding = "utf-8") as filename:
        writer = None
        for i in lists_all:
            output = {"Nickname": i[0], "Fullname": i[1], "Link": "https://kaggle.com/" + i[0], "Points": i[2], "Tier": i[3]}
            if not writer:
                writer = csv.DictWriter(filename, delimiter = ";", fieldnames = output.keys())
                writer.writeheader()
            writer.writerow(output)
    
        print ("Writing completed: file saved in the program directory.")
        
#-----------------------------------PAGE LIMIT MODE---------------------------------------------#            
    
else:
    page_limit = int(input("Set page limit within [1], [2], etc...(each page gives +20 more records): "))
    print("Step: Collecting users, please wait... ")
    
    page = 0
    users_nicknames_list = []
    users_fullnames_list = []
    users_points_list = []
    users_tier_list = []

    while page < page_limit:    
        page = page + 1
        URL = "https://www.kaggle.com/rankings.json?group=" + str(choice) + "&page=" + str(page) + "&pageSize=20"
        r = requests.get(url = URL)
        headers = r.headers
        content = r.json()
        
        content_status = content["list"]
        
        users_nicknames = [i["userUrl"] for i in content["list"]]
        users_nicknames_list.extend(users_nicknames)
        users_nicknames_list_noslash = [i[1:] for i in users_nicknames_list]
    
        users_fullnames = [i["displayName"] for i in content["list"]]
        users_fullnames_list.extend(users_fullnames)
    
        users_points = [i["points"] for i in content["list"]]
        users_points_list.extend(users_points)
    
        users_tier = [i["tier"] for i in content["list"]]
        users_tier_list.extend(users_tier)
    
        git_names_list = []
        git_location_list = []
        git_email_list = []
        git_company_list = []
       
    users_amount = len(users_nicknames_list_noslash)
    print("Collected: " + str(users_amount) + " users")
    
#---------------------------GIT CHECKER [PAGE LIMIT MODE]---------------------------------------# 
    
    print("Step: Checking if users exist on GitHub, please wait ...")    
    for i in users_nicknames_list_noslash:

        headers = {"Authorization": "Token " +  " "} # <== PUT YOUR TOKEN CREDENTIALS  HERE WITH NO SPACES BETWEEN QUOTES
        URL = "https://api.github.com/users/" + i
        r = requests.get(url = URL, headers = headers)
        data = r.json()
        keys = list(data.keys())
        
        if keys[0] != "message":
            git_names_list.append(i)
            git_location_list.append(data["location"])
            git_email_list.append(data["email"])
            git_company_list.append(data["company"])
        else:
            git_names_list.append("null")
            git_location_list.append("null")
            git_email_list.append("null")
            git_company_list.append("null")

    lists_all = list(zip_longest(users_nicknames_list_noslash, users_fullnames_list, users_points_list, users_tier_list, git_names_list, git_location_list, git_email_list, git_company_list))
        
    users_amount = len(users_nicknames_list_noslash)
    print("Checked: " + str(users_amount) + " users")

#---------------------------CSV WRITER [PAGE LIMIT MODE]---------------------------------------#   
    
    print("Step: Saving to CSV ...")
    with open("{}.txt".format(str(input("Enter file name: "))), "w", encoding = "utf-8") as filename:
        writer = None
        for i in lists_all:
            output = {"Nickname": i[0], "Fullname": i[1], "Link": "https://kaggle.com/" + i[0], 
                      "Points": i[2], "Tier": i[3], "GitHub": "https://github.com/" + i[4], "Git-Location": i[5], "Git Email": i[6], "Git Company": i[7]}
            if not writer:
                writer = csv.DictWriter(filename, delimiter = ";", fieldnames = output.keys())
                writer.writeheader()
            writer.writerow(output)

        print("Writing completed: file saved in the program directory.")
