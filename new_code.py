import time
from prettytable import PrettyTable
from colorama import init, Fore, Back, Style
from breeds_dict import logo, breed_group
import random


def generate_prompt_table(field_names, data):
    table = PrettyTable()
    table.field_names = field_names
    for key, value in data.items():
        table.add_row([key, value["name"]])
    print(table)


def display_breed_characteristics(breed_characteristics):
    while True:
        print(Fore.CYAN)
        generate_prompt_table(["Characteristic Number", "Characteristic"], breed_characteristics)
        print(Style.RESET_ALL)

        choice = input("Please choose the characteristic by typing its corresponding number or type '0' to exit: ")

        if choice == '0':
            break

        try:
            choice = int(choice)
            if choice in range(1, len(breed_characteristics) + 1):
                characteristic = breed_characteristics[choice]
                colors = [Fore.GREEN, Fore.MAGENTA, Fore.BLUE, Fore.CYAN]
                color_choice = random.choice(colors)
                print(color_choice + characteristic["value"] + Style.RESET_ALL)
                print()
            else:
                print("Invalid characteristic number. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number or '0' to exit.")


def main():
    init(autoreset=True)
    print(Fore.MAGENTA + "Welcome to the Dog Breed Choice!")
    print(Style.RESET_ALL)
    time.sleep(2)
    print(logo)
    time.sleep(2)
    print(Fore.MAGENTA + "You came here because you want to choose the best dog breed for your family.")
    time.sleep(2)
    print("But first, you need to know that dog breeds are divided into 10 classes as follows:")
    time.sleep(2)

    print(Fore.CYAN)
    generate_prompt_table(["Group Number", "Group Name"], breed_group)
    print(Style.RESET_ALL)

    while True:
        chosen_group_number = input("To learn more about each group, please choose a group number or type '0' to end: ")

        if chosen_group_number == '0':
            print(
                Fore.RED + "Thank you for discovering breed dogs with us! We hope you find the perfect dog for your family!")
            break

        try:
            chosen_group_number = int(chosen_group_number)
            if chosen_group_number in range(1, len(breed_group) + 1):
                group = breed_group[chosen_group_number]
                subgroups = group["subgroups"]

                print(Fore.MAGENTA)
                generate_prompt_table(["Breed Number", "Breed Name"], subgroups)
                print(Style.RESET_ALL)

                while True:
                    breed_nr = input("Please choose a breed number or type '0' to go back: ")

                    if breed_nr == '0':
                        break

                    try:
                        breed_nr = int(breed_nr)
                        if breed_nr in subgroups:
                            breed = subgroups[breed_nr]
                            print(f"You've chosen {breed['name']}!")
                            display_breed_characteristics(breed["characteristics"])
                        else:
                            print("Invalid breed number. Please choose a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a number or '0' to go back.")
            else:
                print("Invalid group number. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number or '0' to end.")


if __name__ == "__main__":
    main()
