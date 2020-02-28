import inputs

def recusive_binary_search(num_list, key, low, high):
    """ This is recursive binary search algorithm"""
    if low >= high:
        return -1

    mid = low + (high - low) // 2
     
    if num_list[mid] == key:
        return mid
    elif num_list[mid] > key:
        return recusive_binary_search(num_list, key, low, mid - 1)
    else:
        return recusive_binary_search(num_list, key, mid + 1, high)  


# num_list = inputs.finite_num_list()   # generates the list of desrired numbers by taking inputs
num_list = inputs.random_num_list_generator() # generates the list of numbers random numbers

num_list.sort() # sorting the list before applying binary search on it.
print("\nThe list after sorting is :\n",num_list)

key = int(input("\nEnter the number you want to find : "))
pos_of_element = recusive_binary_search(num_list, key, 0, len(num_list) - 1) # function call for recursive binary search
print(pos_of_element)

if pos_of_element != -1:
    print(f"{key} is present in list at position {pos_of_element+1}.")
else:
    print(f"{key} is not present in the list.")

