import os
from pathlib import Path
from colorama import init, Fore

init()

print(Fore.GREEN + "This program creates a file and stores contact information on your computer for you to use. Press "
                   "any key to continue...")


def director():
    input()
    print("The default directory on your PC is listed below. \n", (Path.home()))
    print("Folders like Documents, Downloads, and the Desktop live here.")
    file_path = os.path.join(Path.home(),
                             (input("Where would you like to save your file? Enter a folder "
                                    "sub-directory to continue, or press enter to use the default directory: \n")))
    writing = True
    while writing:
        if not os.path.exists(file_path.lower()):
            print(Fore.RED + "You must enter a valid directory")
            director()
        else:
            print(file_path, Fore.GREEN + "is a valid parent directory! Type 'y' create a new subdirectory.")
            confirmation = input()
            if confirmation.lower() == 'y':
                new_folder = input("Type the name of a new folder to create \n")
                file_path = os.path.join(file_path, new_folder)
                os.makedirs(file_path)
                new_file = os.path.join(file_path, (input(f"Type the desired name of your text file to store your "
                                                          f"contact information: \n")))
                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                with open(new_file, 'w+') as f:
                    f.write(input("Please type your name: \n"))
                    f.write(", ")
                    f.write(input("Please type your address: \n"))
                    f.write(", ")
                    f.write(input("Please type your phone number: \n"))
                    f.write(".")
                    os.startfile(new_file)
                    break
            else:
                input(Fore.RED + "You must type 'y' to create a new directory.")


if __name__ == '__main__':
    director()
