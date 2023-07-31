import time
from prettytable import PrettyTable
import pandas as pd
from colorama import Fore, Back, Style, init
import cairn_terrier
import json
from description2 import breed_characteristics, logo, breed_group

group = PrettyTable()
breeds = PrettyTable()
about_characteristics = PrettyTable()

breeds.field_names = ["Breed Number", "Breed"]
group.field_names = ["Group Number", "Group Name"]
group_data = [
    [1, "Sheepdogs and Cattle dogs"],
    [2, "Pinscher and Schnauzer - Molossoid and Swiss Mountain and Cattledogs"],
    [3, "Terriers"],
    [4, "Dachshunds"],
    [5, "Spitz and primitive types"],
    [6, "Scent hounds and related breeds"],
    [7, "Pointing Dogs"],
    [8, "Retrievers - Flushing Dogs - Water Dogs"],
    [10, "Sighthounds"]
]
group.add_rows(group_data)

terrier_breed_options = {
    1: "Airedale Terrier",
    2: "American Pit Bull Terrier",
    3: "Australian Terrier",
    4: "Australian Silky Terrier",
    5: "Cairn Terrier",
    6: "West Highland White Terrier",
    7: "Norfolk Terrier",
    8: "Norwich Terrier",
    9: "Scottish Terrier",
    10: "Scottish Sky Terrier"
}


def show_breeds_in_groups():
    print(Fore.MAGENTA + "Welcome to the Dog Breed Choice!")
    print(Style.RESET_ALL)
    time.sleep(2)
    print(logo)
    time.sleep(2)
    print(Fore.MAGENTA + "You came here because you want to choose the best dog breed for your family.")
    time.sleep(2)
    print(Fore.CYAN + "But first, you need to know that dog breeds are divided into 10 classes as follows:")

    time.sleep(2)
    print(group)
    time.sleep(5)
    chosen_group_number = int(input("To learn more about each group, "
                                    "please choose one of the above by typing the number of the group: \n"))
    print(Style.RESET_ALL)

    if chosen_group_number in breed_group:
        subgroup = breed_group[chosen_group_number]
        subgroup_name = list(subgroup.keys())[0]
        print(subgroup_name)
        sub_breeds = subgroup[subgroup_name]
        print("Breeds:")
        for breed_number, breed_name in sub_breeds.items():
            print(f"{breed_number}: {breed_name}")


def characteristics():
    breed_nr = int(input("Please add the number corresponding to the wanted breed:"))
    for breed in breed_characteristics:
        if breed == terrier_breed_options[breed_nr]:
            print(Fore.CYAN)
            print(f"If you want to know more about the {breed} feel free to explore and get the knowledge"
                  " that interests you.")
            print(Style.RESET_ALL)
            time.sleep(2)
            about_characteristics.field_names = ["Number", "Characteristic"]
            about_characteristics.add_rows(
                [
                    [1, "Description"],
                    [2, "Personality"],
                    [3, "Grooming"],
                    [4, "Living conditions"],
                    [5, "Training"],
                    [6, "Usefulness"],
                ])
            print(about_characteristics)
            print(Style.RESET_ALL)
            end_of_program = False
            while not end_of_program:
                answer = input(Fore.MAGENTA + "\nPlease type the number corresponding to the characteristic ot type 'exit' to end the program: ")
                print(Style.RESET_ALL)
                if answer == "exit":
                    end_of_program = True
                    print(Fore.RED + "End of program")
                else:
                    answer = int(answer)
                    if answer in breed_characteristics[breed]:
                        characteristic = breed_characteristics[breed][answer]
                        print(characteristic)

