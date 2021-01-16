import os
from time import sleep

import pickle # use as a database

def quit():
    try:
        file_object = open('names.pydata', 'wb')
        pickle.dump(names, file_object) # how you pickle data 
        file_object.close()

        # dump(object_to_pickle, where_to_pickle) method to add data to pickle file
        # load(where_to_pickle) method to get data from pickle file

        print("thanks have a good day.")

    except Exception as e:
        print('think but there was an error.')
        print(e)

def createheader():
    os.system('cls')
    print("\t**********************************************")
    print("\t***  Greeter - Hello old and new friends!  ***")
    print("\t**********************************************")

def get_choice():
    choice = ''
    createheader()
    while choice != 'q':    
  
        print("\n[1] See a list of friends.")
        print("[2] Tell me about someone new.")
        print("[q] Quit.")
        
        choice = input("What would you like to do? ")

        if choice == '1':
            print("\nHere are the people I know.\n")
            show_names()
        elif choice == '2':
                print("\nI can't wait to meet this person!\n")
                get_name()
        elif choice == 'q':
                print("\nThanks for playing. Bye.")
                quit()
        else:
                print("\nI didn't understand that choice.\n")

    return choice

def show_names():
   
    print("\nHere are the people I know.\n")
    for name in names:
        print(name.title())
        sleep(0.5)
        
def get_name():

    new_name = input("\nPlease tell me this person's name: ")
    if new_name in names:
        print("\n%s is an old friend! Thank you, though." % new_name.title())
    else:
        names.append(new_name)
        print("\nI'm so happy to know %s!\n" % new_name.title())

# read value from pickle
def load_names():
    try:
        file_object = open('names.pydata', 'rb')
        names = pickle.load(file_object)
        file_object.close()
        return names

    except Exception as e:
        print(e) # print the type of error
        return []

names = load_names()

choice = get_choice()

'''
# add value to pickle
def quit():
    try:
        file_object = open('names.pydata', 'wb')
        pickle.dump(names, file_object) # how you pickle data 
        file_object.close()

        print("thanks have a good day.")

    except Exception as e:
        print('think but there was an error.')
        print(e)
'''

createheader()
if choice == '1':
        print("\nHere are the people I know.\n")
        show_names()
elif choice == '2':
        print("\nI can't wait to meet this person!\n")
        get_name()
elif choice == 'q':
        print("\nThanks for playing. Bye.")
        quit()
else:
        print("\nI didn't understand that choice.\n")