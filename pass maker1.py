import itertools
import os
import sys
from colorama import Fore, Style
from pyfiglet import Figlet

os.system('cls' if os.name == 'nt' else 'clear')

f = Figlet(font='big')
ascii_art = f.renderText('HR Team')
print(Fore.GREEN + ascii_art + Style.RESET_ALL)

print(Fore.BLUE + "___________________________________________________________________" + Style.RESET_ALL) 
print("")
print(Fore.CYAN + "Password List Maker." + Style.RESET_ALL)
print("")
print(Fore.CYAN + "Telegram: @pheraoun" + Style.RESET_ALL)
print(Fore.BLUE + "___________________________________________________________________" + Style.RESET_ALL) 
print("")
print(Fore.RED + "#Note: It is not mandatory to fill out the form completely." + Style.RESET_ALL)
print("")                 
    

def get_input(prompt):
    return input(Fore.YELLOW + prompt + Style.RESET_ALL)
    

def generate_password_list():

    name = get_input("Please enter the target's Name=>  ")
    surname = get_input("Please enter the target's Family name=>  ")
    phone = get_input("Please enter the target's Phone=>  ")
    birth_date = get_input("Please enter the target's Birth date=>  ")
    office_name = get_input("Please enter the target's Office Name=>  ")
    father_name = get_input("Please enter the target's Father's Name=>  ")
    city = get_input("Please enter the target's City (name)=>  ")
    


    info_list = [name, surname, phone, birth_date, office_name, father_name, city]
    

    filtered_info = [info for info in info_list if info]


    count = int(get_input("لطفا تعداد پسوردهایی که می‌خواهید تولید شود را وارد کنید: "))
    

    passwords = set()


    if not filtered_info:
        print(Fore.RED + "هیچ اطلاعاتی برای تولید پسورد وجود ندارد." + Style.RESET_ALL)
        return

    for i in range(1, len(filtered_info) + 1):
        combinations = itertools.combinations(filtered_info, i)
        for combo in combinations:
            passwords.add(''.join(combo))

    password_list = list(passwords)[:count]

    
    print(Fore.GREEN + "\nپسوردهای تولید شده:" + Style.RESET_ALL)
    for password in password_list:
        print(password)

if __name__ == "__main__":
    generate_password_list()