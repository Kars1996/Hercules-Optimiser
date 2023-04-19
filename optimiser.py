import os, getpass
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
getpass.getpass(prompt=blue('        [+] Press enter to exit the program'))
quit()
