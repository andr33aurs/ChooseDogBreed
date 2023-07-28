import time
from prettytable import PrettyTable
import pandas as pd
from colorama import Fore, Back, Style, init
import cairn_terrier
import json

group = PrettyTable()
breeds = PrettyTable()
breeds.field_names = ["Breed Number", "Breed"]
group.field_names = ["Group Number", "Group Name"]
group.add_rows(
    [
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
)


def starting():
    print(Fore.MAGENTA + "Welcome to the Dog Breed Choice!")
    print(Style.RESET_ALL)
    time.sleep(2)
    print('''
    ********************************************          
                        |\|\
                       ..    \       .
                     o--     \\    / @)
                      v__///\\\\__/ @
                        {           }
                         {  } \\\{  }
                         <_|      <_|
    ********************************************
    ''')
    time.sleep(2)
    print(Fore.MAGENTA + "You came here because you want to choose the best dog breed for your family.")
    time.sleep(2)
    print(Fore.CYAN + "But first, you need to know that dog breeds are divided into 10 classes as follows:")

    time.sleep(2)
    print(group)
    time.sleep(5)
    chosen_group = input("To learn more about each group, "
                         "please choose one of the above by typing the number of the group: \n")
    print(Style.RESET_ALL)
    if chosen_group == "3":
        print(Fore.MAGENTA + "Excellent choice!!!")
        breeds.field_names = ["Breed Number", "Breed"]
        breeds.add_rows(
            [
                [1, "Airedale Terrier"],
                [2, "American Staffordshire Terrier"],
                [3, "Australian Terrier"],
                [4, "Australian Silky Terrier"],
                [5, "Cairn Terrier"],
                [6, "West Highland White Terrier"],
                [7, "Norfolk Terrier"],
                [8, "Norwich Terrier"],
                [9, "Scottish Terrier"],
                [10, "Scottish Sky Terrier"]
            ]
        )
        print(breeds)

    elif chosen_group == "4":
        print("Excellent choice!!!")
        breeds.add_rows(
            [
                [1, "Dachshund"],
                [2, "Dachshund -The Wiry Hair Variety"],
                [3, "Long-Haired Dachshund"]
            ]
        )


breed_options = {
    1: "Airedale Terrier",
    2: "American Staffordshire Terrier",
    3: "Australian Terrier",
    4: "Australian Silky Terrier",
    5: "Cairn Terrier",
    6: "West Highland White Terrier",
    7: "Norfolk Terrier",
    8: "Norwich Terrier",
    9: "Scottish Terrier",
    10: "Scottish Sky Terrier"
}

about_breed = {
    1: "Description",
    2: "Personality",
    3: "Grooming",
    4: "Living situation",
    5: "Training",
    6: "Usefulness"
}


def chosen_breed():
    print("Now that you have seen how many dog breeds are included in the 3rd Group,"
          "Please be free to explore the characteristics of each breed. \n"
          "These information will help you choose the most suitable companion for you and your family.")
    breed_nr = int(input("In order to do that, please choose the number corresponding to the dog breed you want to "
                         "know: "))

    if breed_nr in breed_options:
        print(breed_options[breed_nr])

        # breed_file, breed_function = breed_options[breed_nr]
        # function_to_call = getattr(breed_file, breed_function)
        # function_to_call()
    # if breed_nr == 5:
    #     characteristics()


def characteristics():
    choice = int(input("If you want to know more about this breed, feel free to explore and get the knowledge"
                       " that interests you by typing its number: "))
    if choice in about_breed:
        print(about_breed[choice])

    # if choice == 1:
    #     print("")
    #     print(cairn_terrier.personality())
    # elif choice == 2:
    #     print(cairn_terrier.grooming())
    # elif choice == 3:
    #     print(cairn_terrier.living_conditions())
    # elif choice == 4:
    #     print(cairn_terrier.training())
    # elif choice == 5:
    #     print(cairn_terrier.usefulness())
