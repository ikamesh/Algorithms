import inputs

def linear_search(num_list, key):
    for num in num_list:
        if num == key:
            return num_list.index(num)
    return -1


num_list = inputs.random_num_list_generator() #this genrates list of given l
key = int(input("\nEnter an element to find its position in the list : "))


pos_of_element = linear_search(num_list, key)

if pos_of_element != -1 :
    print(f"\n\t{key} is at present at position {pos_of_element+1}.\n")
else:
    print(f"\n\t{key} is not present in the list")




    

    