import time
from prettytable import PrettyTable
from colorama import Fore, Back, Style, init
from description2 import logo, breed_group


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
    chosen_group_number = int(input("To learn more about each group, "
                                    "please choose one of the above by typing the number of the group: \n"))

    group = breed_group[chosen_group_number]
    # print(group["name"])
    subgroups = group["subgroups"]

    # for breed_key, breed_value in subgroups.items():
    #     print(f"{breed_key}: {breed_value['name']}")
    print(Fore.MAGENTA)
    generate_prompt_table(["Breed Number", "Breed Name"], subgroups)
    print(Style.RESET_ALL)
    breed_nr = int(input("Please add the number corresponding to the wanted breed:"))
    breed = subgroups[breed_nr]
    breed_characteristics = breed["characteristics"]

    # for characteristic_key, characteristic_value in breed_characteristics.items():
    #     print(f"{characteristic_key}: {characteristic_value['name']}")
    print(Fore.CYAN)

    generate_prompt_table(["Characteristic Number", "Characteristic"], breed_characteristics)
    print(Style.RESET_ALL)
    end_of_program = False
    while not end_of_program:
        characteristic_nr = input("Please choose the characteristic by typing its corresponding number or type 'Exit' to end:")
        if characteristic_nr.lower() == "exit":
            end_of_program = True
            print(Fore.RED + "End of program" + Style.RESET_ALL)
        else:
            characteristic_nr = int(characteristic_nr)
            print(Fore.LIGHTGREEN_EX)
            characteristic = breed_characteristics[characteristic_nr]
            print(characteristic["value"])
