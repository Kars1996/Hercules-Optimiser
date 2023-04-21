import os, getpass
import webbrowser
#https://discord.gg/kWZ8G4wYnS
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
    print(blue('        [!] Please select either Y or N'))
    print(blue('        [?] Would you like to join the discord? [Y/N]'))
    Discord_Join = input(str('        > ')).lower()
if Discord_Join == 'y':
    print(blue('        [$] Opening the discord'))
    webbrowser.open('https://discord.gg/kWZ8G4wYnS')
    getpass.getpass(prompt=blue('        [+] Press enter to exit the program'))
    quit()
if Discord_Join == 'n':
    getpass.getpass(prompt=blue('        [+] Press enter to exit the program'))
    quit()


