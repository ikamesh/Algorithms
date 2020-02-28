import random 

"""This is file for generating input list for algorithms"""

#input method1 -- filling list with try-except
def infinite_num_list():
    print("""
Press enter after each input.
Press 'x' to when done...!
        """)

    num_list = [] 
    while True:
        num = input("Enter num to fill the list : ")
        if type(num) == 'int':
            num_list.append(num)
        elif num.lower() == "x":
            break
        else:
            pass
    
    return num_list


# input method2 -- filling element with for loop
def finite_num_list():
    num_of_element = int(input("\nHow many elements do you have..? : "))
    print(f"Enter {num_of_element} elements :")

    num_list = []
    for _ in range(num_of_element):
        num_list.append(int(input()))

    return num_list


# Input Method3 -- Generating num with random
def random_num_list_generator():
    num_of_element = int(input("\nHow many num in list you want to generate : "))

    num_list = []
    for _ in range(num_of_element):
        num_list.append(random.randint(0, num_of_element))

    if input("\nDo you want to print the list (Y/N): ").lower() == "y":
        print("\n", num_list)
    
    return num_list


if __name__ == "__main__":
    infinite_num_list()
    finite_num_list()
    random_num_list_generator()
