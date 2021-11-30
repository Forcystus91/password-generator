import random
import os.path
from os import path
import csv


def main():
    password_creator()


def password_creator():
    """if path.exists(<desired_location>) == False:  # Creates header for the file
        save_path = <location_on_disk>
        name_of_file = <desired_name_of file>
        complete_name = os.path.join(save_path,name_of_file+".csv")
        header = ['Site','Username','Password']
        f = open(complete_name,"a+")
        writer = csv.writer(f,lineterminator='\n')
        writer.writerow(header)
        f.close()
        """

    site = input("Where will this password be used? ")
    username = input("Username: ")
    length = int(input("How many characters in password? "))
    password = ""
    while len(password) < length:
        for i in range(length):
            if i < 1:  # Gives the password one special character
                char1 = random.randint(33,47)
                password = password + chr(char1)
            elif i < 3:  # gives the password two numbers
                char_num = random.randint(48,57)
                password = password + chr(char_num)
            else:  # fills the remaining characters in the password with letters
                char2 = random.randint(65,90)    
                char3 = random.randint(97,122)
                dice = random.randint(1,2)
                if dice == 1:
                    password = password + chr(char2)
                else:
                    password = password + chr(char3)
        
        shuffled_password = ''.join(random.sample(password,len(password)))  # Shuffles the password

    """save_path = <location_on_disk>
    name_of_file = <desired_name_of_file>
    complete_name = os.path.join(save_path,name_of_file+".csv")
    f = open(complete_name,"a")
    writer = csv.writer(f,lineterminator='\n')
    data = [site, username, shuffled_password]
    writer.writerow(data)
    f.close()"""


main()