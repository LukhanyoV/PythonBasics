#Lukhanyo Vakele
#This is my script
#That will help me grab saved WiFi names in a Windows machine
#Hopefully I can make it grab the passwords too :P

#we are going to need to execute some commands with the system
import os

#now let's first grab the WiFi names and store in a temp file
os.system("netsh wlan show profiles > temp_file.txt")

#initialize the container for the filtered wifi names
filtered_wifi_names = []

#now then lets open the temp_file.txt and filter out all the unwanted info
with open("temp_file.txt","r") as tempFile:
    lines = tempFile.readlines()
    #loop through the lines in temp_file.txt
    #and grab only the WiFi network names
    for line in lines:
        #grab the results with a specific pattern
        if "All User Profile     : " in line:
            #grab everything after a specific character
            wifi = line.split("All User Profile     : ",1)[-1]
            wifi = wifi.rstrip()
            filtered_wifi_names.append(wifi)
        
#we don't need temp_file.txt anymore let's delete it
os.remove("temp_file.txt")

#now lets check if there are any filtered wifi names
#when am trying to find the saved passwords it will be much easier
if len(filtered_wifi_names) != 0:
    print("There are currently",len(filtered_wifi_names),"WiFi networks saved on this machine")
    print("Please wait while I find the passwords")
    print("Your screen may blink at you, but that's normal")
    #now then I have the WiFi network names filtered
    #all I got to do now is look for the password for each network
    #and save the results in a file called WiFi Password.txt
    # print(filtered_wifi_names)
    for wifi_name in filtered_wifi_names:
        #now formart the name of the wifi in the command to be executed by the system
        command = "netsh wlan show profiles name=\"%s\" key=clear | findstr \"Key Content\" >> temp_pass.txt" % (wifi_name)
        #to be continued, P.S. try to figure out how you are going to write to file
        #my idea was to concancinate wifi name and password but grabing the password might be a small challenge
        # print(command)
        os.system(command)

    #and also open the file that currently contains the passwords we are going to take the
    with open("temp_pass.txt","r") as passFile:
        #now lets get each line
        lines = passFile.readlines()
        #now lets filter out the passwords
        filtered_passwords = [] # I will store the filtered passwords in here
        #now then let us grab the passwords and then append them to my list
        for line in lines:
            password = line.split(": ",1)[-1]
            password = password.rstrip()
            filtered_passwords.append(password)

    # lets open a new file where we are going to store the WiFi name and the password next to it
    with open("WiFi Passwords.txt","w") as saveFile:

        #now we have two lists the WiFi name list and the list that contains the passwords
        #they are both separated but now I want them on the same file 

        #using a for loop and if statement am going to match the passwords where they belong
        if len(filtered_passwords) == len(filtered_wifi_names):
            for x in range(len(filtered_passwords)):
                wife = filtered_wifi_names[x]
                passwd = filtered_passwords[x]
                if passwd == "1":
                    passwd = "Wi-Fi has no password"
                    saveFile.write(wife+" : "+passwd+"\n")
                else:
                    saveFile.write(wife+" : "+passwd+"\n")
                    
        # delete the temp pass file
        os.remove("temp_pass.txt")       
else:
    #tell the user that there are no WiFi networks saved on this machine
    print("There is currently no WiFi saved on this machine")
    
