import time
from prettytable import PrettyTable
from colorama import Fore, Back, Style, init
from breeds_dict import logo, breed_group
import random


def generate_prompt_table(field_names, groups):
    groups_table = PrettyTable()
    groups_table.field_names = field_names
    for group_key, group_value in groups.items():
        groups_table.add_row([group_key, group_value["name"]])
    print(groups_table)


def show_breeds_in_groups():
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

    choose_breed = True
    while choose_breed:
        chosen_group_number = int(input("To learn more about each group, "
                                        "please choose one of the above by typing the number of the group or type '0 to end the program: "))
        if chosen_group_number == 0:
            choose_breed = False
            print(
                Fore.RED + "Thank you for discovering breed dogs with us! We hope that you will choose the best dog for you and your family!")
        elif chosen_group_number in range(len(breed_group) + 1):
            group = breed_group[chosen_group_number]

            # print(group["name"])
            subgroups = group["subgroups"]

            for breed_key, breed_value in subgroups.items():
                breed_name = breed_value['name']
                breed_key = breed_key
                # print(f"{breed_key}: {breed_value['name']}")

            print(Fore.MAGENTA)
            generate_prompt_table(["Breed Number", "Breed Name"], subgroups)
            print(Style.RESET_ALL)

            breed_nr = int(input("Please add the number corresponding to the wanted breed:"))
            breed = subgroups[breed_nr]
            chosen_breed_from_subgroup = int(input(
                "Excellent choice! In order to find out more about the chosen breed take a look at these characteristics or type '0' to choose another breed: "))

            while chosen_breed_from_subgroup:

                breed_characteristics = breed["characteristics"]

                # for characteristic_key, characteristic_value in breed_characteristics.items():
                #     print(f"{characteristic_key}: {characteristic_value['name']}")
                if chosen_breed_from_subgroup == 0:
                    print(int(input("Please choose another breed by typing its corresponding number: ")))
                print(Fore.CYAN)
                generate_prompt_table(["Characteristic Number", "Characteristic"], breed_characteristics)
                print(Style.RESET_ALL)

                end_of_program = False
                while not end_of_program:
                    characteristic_nr = int(input(
                        "Please choose the characteristic by typing its corresponding number or type '0'to exit the program: "
                        "to end the program:"))
                    if characteristic_nr == 0:
                        end_of_program = True
                        print(Fore.RED + "End of program" + Style.RESET_ALL)
                    elif characteristic_nr in range(len(breed_characteristics) + 1):
                        characteristic_nr = int(characteristic_nr)
                        characteristic = breed_characteristics[characteristic_nr]
                        colors = [Fore.GREEN, Fore.MAGENTA, Fore.BLUE, Fore.CYAN]
                        color_choice = random.choice(colors)
                        print(color_choice + characteristic["value"] + Style.RESET_ALL)
                        print()
                    else:
                        characteristic_nr = int(input(
                            "Please choose the characteristic by typing its corresponding number or type '0'to go back and choose another breed: "
                            "to end the program:"))




        elif chosen_group_number == 0:
            choose_breed = False
            print(
                Fore.RED + "Thank you for discovering breed dogs with us! We hope that you will choose the best dog for you and your family!")
