import time

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
print("Welcome to the Dog Breed Choice!")
print("You came here because you want to choose the best dog breed for your family.")
print("But first, you need to know that dog breeds are divided into 10 classes as follows:")
print("*" * 83)
time.sleep(1)
print("Group 1. Sheepdogs and Cattle dogs")
print("-" * 83)
time.sleep(1)
print("Group 2. Pinscher and Schnauzer - Molossoid and Swiss Mountain and Cattledogs")
print("-" * 83)
time.sleep(1)
print("Group 3. Terriers")
print("-" * 83)
time.sleep(1)
print("Group 4. Dachshunds")
print("-" * 83)
time.sleep(1)
print("Group 5. Spitz and primitive types")
print("-" * 83)
time.sleep(1)
print("Group 6. Scent hounds and related breeds")
print("-" * 83)
time.sleep(1)
print("Group 7: Pointing Dogs")
print("-" * 83)
time.sleep(1)
print("Group 8. Retrievers - Flushing Dogs - Water Dogs")
print("-" * 83)
time.sleep(1)
print("Group 9. Companion and Toy Dogs")
print("-" * 83)
time.sleep(1)
print("Group 10. Sighthounds")
print("*" * 83)
time.sleep(1)

chosen_group = input("To learn more about each group, "
                     "please choose one of the above by typing the number of the group: \n")

if chosen_group == "1":
    print("")

print("Now that you've learned the group's characteristics, "
      "you can move forward and discover the dog breeds belonging to each individual group.")
chosen_group = input("Please choose the group that interests you by typing its number:\n")

if chosen_group == 1:
    print("A herding dog, also known as a stock dog, shepherd dog, sheep dog or working dog, "
          "is a type of dog that either has been trained in herding or belongs to breeds that are developed for "
          "herding.")

if chosen_group == 2:
    print("The dogs from this class are generally pretty big (there are also exceptions), lonely, gentle with friends "
          "and family, but aggressive when they are challenged."
          "Besides the watchdog and protection dog functions, they are also good companions."
          "Who wants a dog from this class, must not forget about its sizes, "
          "its needs for food, space, training, which are bigger than for a small sized dog."
          "Dogs from this class are recommended especially to persons with experience in raising dogs, "
          "who understands the character and needs of dogs. "
          "It must be socialized since an early age, with a firm, consequent, varied training, but also friendly, "
          "a devoted and stable friend can be obtained.")

# it's time to choose a dog breed according to your needs and wishes.



