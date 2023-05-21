from cryptography.fernet import Fernet
from colorama import Fore
import colorama
import csv
import os


colorama.init(autoreset=True)
print(Fore.BLUE + "Welcome to the password manager!😃")

def main():
    key = b'6wFxOLQxDXvi5UqeIzJ9886-23geqARprsLSSBqJ82Q='
    f = Fernet(key)
    main_menu(f)
    while True:
        cont = input(Fore.YELLOW + "Do you want to continue? (y/n): ")
        cont = cont.lower().strip()
        if cont == "y" or cont == "yes":
            main()
        elif cont == "n" or cont == "no":
            print(Fore.BLUE + "Thank you for using SecureVault Your passwords are now safely stored. Have a great day!")
            exit()
        else:
            print(Fore.RED + "Error: Invalid input. please enter (y/n).")
            pass


def retrieve_one(f,site,email):
    try:
        with open("secrets.csv","r") as file:
            reader = csv.DictReader(file)
            for dict in reader:
                if dict["site"] == site and dict["email"] == email:
                    buffer = str(dict["hash"][2:-1])
                    buffer = buffer.encode()
                    buffer = f.decrypt(buffer)
                    print(Fore.GREEN + f"password is {str(buffer)[2:-1]}")
                    return True
            print(Fore.RED + "Error: Account not found.")
            return False
    except (FileNotFoundError):
        print(Fore.RED + "Error: file not found you should add an account before retrievement.")
        return False


def retrieve_all(f):
    # Return all accounts and hashes
    result = []
    try:
        with open("secrets.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                result.append(row)
        if len(result) == 0:
            print(Fore.RED + "Error: No accounts found.")
            return False
        for secret in result:
            buffer = str(secret["hash"][2:-1])
            buffer = buffer.encode()
            buffer = f.decrypt(buffer)
            print(Fore.GREEN + f"[{secret['site']}] account's [{secret['email']}] and it's password's [{str(buffer)[2:-1]}]")
        return True
    except FileNotFoundError:
        print(Fore.RED + "Error: file not found, you should add an account before retrievement.")
        return False



def add(f,site, account, password):
    # check if the file exists
    if os.path.exists("secrets.csv") == False:
        open("secrets.csv", "x")
        with open ("secrets.csv","w") as file:
            writer = csv.DictWriter(file,fieldnames = ["site","email","hash"])
            writer.writerow({"site":"site","email":"email","hash":"hash"})

    # add an account and hash to the file if it doesn't exist
    try:
        if not site or not account or not password:
            print(Fore.RED + "Error: one or more fields are empty.")
            return False
        if is_exist(site,account):
            raise ValueError
        with open("secrets.csv", "a") as file:
            writer = csv.DictWriter(file,fieldnames=["site","email", "hash"])
            b = f.encrypt(bytes(password,'utf-8'))
            writer.writerow({"site" :site ,"email":account, "hash":b})
        return True
    except ValueError:
        print(Fore.RED + "Error: Account already exists.")
        return False


def delete_one(site, email):
    # delete a single account
    flag = False
    try:
        secrets = []
        with open("secrets.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                secrets.append(row)
        if len(secrets) == 1 and secrets[0]["email"] == email and secrets[0]["site"] == site:
            os.remove("secrets.csv")
            return True
        else:
            with open("secrets.csv", "w") as file:
                writer = csv.DictWriter(file,fieldnames=["site","email", "hash"])
                writer.writerow({"site":"site","email":"email","hash":"hash"})
                for secret in secrets:
                    if secret["site"] == site and secret["email"] == email:
                        flag = True
                    else:
                        writer.writerow(secret)
                if flag == True:
                    return True
                else:
                    print(Fore.RED + "Error: Account not found.")
                    return False
    except FileNotFoundError:
        print(Fore.RED + "Error: no file created you should add a password before deleting")
        return False


def delete_all():
    try:
        os.remove("secrets.csv")
        print(Fore.GREEN + "All accounts deleted successfully.")
        return True
    except FileNotFoundError:
        print(Fore.RED + "Error: no file created you should add a password before deleting")
        return False


def update(f,site,account,password):
    try:
        if is_exist(site,account):
            # updating = delete + add the record updated
            delete_one(site,account)
            add(f,site,account,password)
            print(Fore.GREEN + "Account updated successfully.")
            return True
        else:
            # false if the record doesnt exist
            print(Fore.RED + "Error: Account not found.")
            return False
    except FileNotFoundError:
        # handling user error in case user choose update without adding any records
        print(Fore.RED + "Error: no file created you should add a password before updating")
        return False


def choose(max):
    """make sure the user enters the right input"""
    while True:
        try:
            choice = input(Fore.YELLOW + "choose an option : ").strip()
            if not choice.isdigit() or int(choice) < 1 or int(choice) > max:
                raise ValueError
            choice = int(choice)
        except ValueError :
                print(Fore.RED + f"Error: Invalid input. please enter a number between 1 and {max}.")
                pass
        else :
            return choice



def main_menu(f):
    """make user choose an option and handle translating between methods"""
    print("Please choose an option:")
    print("1. Retrieve a password ")
    print("2. Retrieve all passwords")
    print("3. Add a password")
    print("4. Delete a password")
    print("5. Delete all passwords")
    print("6. Update a password")
    print("7. about SecureVault")
    print("8. Exit")
    choice = choose (8)
    match choice:
        case 1:
            site = input("Enter the site's name: ")
            email = input("Enter the email: ")
            retrieve_one(f,site,email)
        case 2:
            return retrieve_all(f)
        case 3:
            site = input("Enter site's name: ")
            account = input("Enter account or username: ")
            password = input("Enter password: ")
            added = add(f, site, account, password)
            # if add method returned false the user is routed to the next menu
            while not added:
                print("select one of the following options:")
                print("1. Try again")
                print("2. Update the password")
                print("3. Return to main menu")
                choice = choose(3)
                match choice:
                    case 1:
                        site = input("Enter the site name: ")
                        account = input("Enter the account name: ")
                        password = input("Enter the password: ")
                        return add(f,site,account,password)
                    case 2:
                        password = input(f"Enter new password for [{site}] with account [{account}] : ")
                        return update(f,site,account,password)
                    case 3:
                        return main_menu(f)
        case 4:
            site = input("Enter the site's name: ")
            account = input("Enter the account's name: ")
            deleted = delete_one(site, account)
            if deleted:
                print(Fore.GREEN + "Account deleted successfully.")
            while not deleted:
                print("select one of the following options:")
                print("1. Try again")
                print("2. retrieve all accounts")
                print("3. Return to main menu")
                choice = choose(3)
                match choice:
                    case 1:
                        site = input("Enter the site's name: ")
                        account = input("Enter the account's name: ")
                        deleted = delete_one(site, account)
                    case 2:
                        return retrieve_all(f)
                    case 3:
                        return main_menu(f)
        case 5:
            while True:
                try:
                    answer = input("are you sure ? (y/n)")
                    if answer.lower() not in ["y","yes","n","no"]:
                        raise ValueError
                    elif answer in ["y","yes"]:
                        delete_all()
                    else:
                        main_menu(f)
                except ValueError:
                    print("invalid input")
                else:
                    break
        case 6:
            site = input("Enter the site's name: ")
            account = input("Enter the account name: ")
            password = input("Enter the password: ")
            update(f,site, account, password)
        case 7:
            print(" Introducing our new terminal Python manager app, designed to simplify your life by securely storing and managing all your passwords in one place.\n With a user-friendly interface, this app allows you to easily add, delete, update and reveal passwords with just a few clicks.\n The program ensures the safety of your sensitive information by hashing your password before storing it in a file,\n making it virtually impossible for anyone to access without the correct credentials. Whether you're managing multiple accounts or just looking\n for a secure way to store your passwords, our Python manager app is the perfect solution.\n Try it out today and experience the peace of mind that comes with knowing your passwords are safe and easily accessible whenever you need them.")
        case 8:
            print(Fore.BLUE + "Thank you for using SecureVault Your passwords are now safely stored. Have a great day!")
            exit()


def is_exist(site,email):
    """ a method to check if an account exists in secrets.csv"""
    with open("secrets.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["site"] == site and row["email"] == email:
                return True
        return False


if __name__ == "__main__":
    main()