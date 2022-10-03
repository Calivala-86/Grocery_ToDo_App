

USER_INPUT = " "  # For users to input info

grocery = []  # Create an empty list to store the final result

def update_file(list):
    ''' Creating a file '''
    try:
        with open("Grocery_Bud.txt", "w") as file:
            file.write(list)
    except FileNotFoundError:
        print("The 'docs' directory does not exist")


def read_file():
    ''' Function to read an existing file '''
    try:
        with open('Grocery_Bud.txt') as file:
            file.read()
    except IOError:
        print("File not not found or not accessible")

def list_to_dict(list):
    """ Converting a list to dictionary"""
    my_grocery=dict()
    for key, value in enumerate(list):
        my_grocery[key] = value
        
    return my_grocery 
    
def dict_to_list(dict):
    """Converting a dictionary to list"""
    new_list = list(dict.values())
    return new_list            

def show_menu():
    """ Simple menu for user's selection """

    print("\n======= Grocery Bud ========\n")
    print("Option 1. Add an item: ")
    print("Option 2. Remove an item: ")
    print("Option 3. Edit an item: ")
    print("Option 4. Show grocery list: ")
    print("Option 5. Clear the list: ")
    print("Option 6. Exit/Restart: ")


while USER_INPUT != "6":

    show_menu()
    USER_INPUT = input("\nSelect your option: ")
    my_grocery = (list_to_dict(grocery))
    
    if USER_INPUT == "1":
        """" Initiate the list """
        
        item = input("e.g Rice ")
        grocery.append(item.capitalize())
        
    elif USER_INPUT == "2":
        """ Option to delete an item in the list """
         
        print("Items on the list: ",my_grocery)
        key = int(input("Enter a key: "))
        print(my_grocery.pop(key,"Key does not exists"))
        print(my_grocery)
        grocery = dict_to_list(my_grocery)
        print(grocery)
        
    elif USER_INPUT == "3":
        """ Option to edit/rename/change an item in the list """
        
        print("Items on the list: ",my_grocery)
        key = int(input("Enter a key: "))
        
        for i in my_grocery.keys():   
            if key == i:
                value = str(input("Enter new item: "))  
                my_grocery[key]=value.capitalize()
                grocery = dict_to_list(my_grocery)
                print(grocery) 
                break   
        else:
            print("Key does not exists")  
                         
    elif USER_INPUT == "4":
        """ Display the list of items """
        
        print("Grocery list: ")
        print(grocery)            
             
    elif USER_INPUT == "5":
        """ Clear up the list """
        print("Clear Items ")
        grocery.clear()
        print("List is empty. Please enter your list")      
        
    elif USER_INPUT == "6":
        """ Exit/Continue """
        
        restart = input("Let's do next grocery list? (yes/no): ")
        if restart == "no":
            print("Goodbye..")
            break
        USER_INPUT = input("Select your option: ")
        
    # Calling the to create/update the file
    update_file(str(grocery))

# Reading the file 
read_file()



    
