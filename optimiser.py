#Coming Soon :D
import os, getpass
import webbrowser

def blue(text):
    os.system(""); faded = ""
    for line in text.splitlines():
        green = 0
        for character in line:
            green += 3
            if green > 255:
                green = 255
            faded += (f"\033[38;2;0;{green};255m{character}\033[0m")
        faded += "\n"
    return faded

banner = '''                  :::    ::: :::::::::: :::::::::   ::::::::  :::    ::: :::        :::::::::: :::::::: 
                 :+:    :+: :+:        :+:    :+: :+:    :+: :+:    :+: :+:        :+:       :+:    :+: 
                +:+    +:+ +:+        +:+    +:+ +:+        +:+    +:+ +:+        +:+       +:+         
               +#++:++#++ +#++:++#   +#++:++#:  +#+        +#+    +:+ +#+        +#++:++#  +#++:++#++   
              +#+    +#+ +#+        +#+    +#+ +#+        +#+    +#+ +#+        +#+              +#+    
             #+#    #+# #+#        #+#    #+# #+#    #+# #+#    #+# #+#        #+#       #+#    #+#     
            ###    ### ########## ###    ###  ########   ########  ########## ########## ########       '''

os.system('cls' if os.name == 'nt' else 'clear')
print(blue(banner))
print(blue('        [$] Under Construction'))
print(blue('        [?] Would you like to join the discord for updates? [Y/N]'))
Discord_Join = input(str('        > ')).lower()
while Discord_Join not in ['y', 'n']:
    print(blue('        [!] Error: Please select either "Y" or "N"'))
    print(blue('        [?] Would you like to join the discord? [Y/N]'))
    Discord_Join = input(str('        > ')).lower()
if Discord_Join == 'y':
    print(blue('        [$] Opening the discord'))
    webbrowser.open('https://discord.gg/vZvMUqjQcp')
    print(blue('        [?] Would you like to check out the trello? [Y/N]'))
    trello_link = input(str('        > ')).lower()
    while trello_link not in ['y', 'n']:
        print(blue('        [!] Error: Please select either "Y" or "N"'))
        print(blue('        [?] Would you like to check out the trello? [Y/N]'))
        trello_link = input(str('        > ')).lower()       
    if trello_link == 'y':
        print(blue('        [$] Opening Trello Link')) 
        webbrowser.open('https://trello.com/b/QG5KYXsv/todo')
        getpass.getpass(prompt=blue('        [+] Press enter to exit the program'))
        quit
    if trello_link == 'n':
        getpass.getpass(prompt=blue('        [+] Press enter to exit the program'))
        quit
if Discord_Join == 'n':
    print(blue('        [?] Would you like to check out the trello? [Y/N]'))
    trello_link = input(str('        > ')).lower()
    while trello_link not in ['y', 'n']:
        print(blue('        [!] Error: Please select either "Y" or "N"'))
        print(blue('        [?] Would you like to check out the trello? [Y/N]'))
        trello_link = input(str('        > ')).lower()       
    if trello_link == 'y':
        print(blue('        [$] Opening Trello Link')) 
        webbrowser.open('https://trello.com/b/QG5KYXsv/todo')
        getpass.getpass(prompt=blue('        [+] Press enter to exit the program'))
        quit
    if trello_link == 'n':
        getpass.getpass(prompt=blue('        [+] Press enter to exit the program'))
        quit
