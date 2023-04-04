import os

def adduser_name(): 
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to add: ")
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
    if confirm == "y":
        print("code running successfully")
    else:
        print("no")
        
    
adduser_name()