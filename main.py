import requests , os , platform, colorama
from colorama import Fore

if platform.system == ("linux"):
    os.system("clear")
else:
    os.system("title Webhook sender")
    os.system("cls")
def sim_web():
    print (f"""{Fore.RED}
 __   __  ___   _______  _______    __    __     ______      ______    __   ___     
|"  |/  \|  "| /"     "||   _  "\  /" |  | "\   /    " \    /    " \  |/"| /  ")    
|'  /    \:  |(: ______)(. |_)  :)(:  (__)  :) // ____  \  // ____  \ (: |/   /     
|: /'        | \/    |  |:     \/  \/      \/ /  /    ) :)/  /    ) :)|    __/      
 \//  /\'    | // ___)_ (|  _  \\  //  __  \\(: (____/ //(: (____/ // (// _  \      
 /   /  \\   |(:      "||: |_)  :)(:  (  )  :)\        /  \        /  |: | \  \     
|___/    \___| \_______)(_______/  \__|  |__/  \"_____/    \"_____/   (__|  \__)    
                                                                                    
          ________  _______  _____  ___   ________    _______   _______             
         /"       )/"     "|(\"   \|"  \ |"      "\  /"     "| /"      \            
        (:   \___/(: ______)|.\\   \    |(.  ___  :)(: ______)|:        |           
         \___  \   \/    |  |: \.   \\  ||: \   ) || \/    |  |_____/   )           
          __/  \\  // ___)_ |.  \    \. |(| (___\ || // ___)_  //      /            
         /" \   :)(:      "||    \    \ ||:       :)(:      "||:  __   \            
        (_______/  \_______) \___|\____\)(________/  \_______)|__|  \___)           
{Fore.WHITE}""")
    webb = input(f'[ {Fore.RED}+{Fore.WHITE} ] Enter Webhook :{Fore.RED} ')
    avaa = input(f'{Fore.WHITE}[ {Fore.RED}+{Fore.WHITE} ] Enter Avatar url :{Fore.RED} ')
    user = input(f'{Fore.WHITE}[ {Fore.RED}+{Fore.WHITE} ] Enter Username :{Fore.RED} ')
    while True:
        try:
            webhook = (webb)
            avatar = (avaa)
            username = (user)
            message = input(f"\n{Fore.WHITE}[ {Fore.RED}+{Fore.WHITE} ] Enter Message :{Fore.RED} ")
            data = requests.post(webhook, json={'content': message, 'avatar_url': avatar, "username": username})

            if data.status_code == 204:
                print(f'{Fore.WHITE}\n' 'Sent : ' + message)
                print(f'{Fore.WHITE} To : ' + webb, '\n')
                cd = input("To stop Enter (1) or to continue enter (2) : ")
                if cd =='1':
                    break
                if cd =='2':
                    continue
            else:
                data = requests.post(webhook, json={'content': message, "username": username})
                if data.status_code == 204:
                 print(f'{Fore.WHITE} \n' 'Sent : ' + message)
                 print('To : ' + webb, '\n')
                 cd = input("To stop Enter (1) or to continue enter (2) : ")
                 if cd =='1':
                     break
                 if cd =='2':
                     continue
                else:
                    print("\nWebhook Error or Deleted!\n-> " + webhook)
                    break
        except:
            print('\nSomething happend! / cannot connect to the webhook.')
            break

sim_web()