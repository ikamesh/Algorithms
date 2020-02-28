import inputs

def binary_search(num_list, key, low, high):
    """ This is function for iterative binary searching """

    while low <= high: 

        mid = low + (high - low) // 2

        if num_list[mid] == key:    #if element is found at mid 
            return mid
        
        elif num_list[mid] <= key:  # if element is present after mid, new low is mid+1
            low = mid + 1
        
        else:   # if element is present before mid, we change high to mid-1
            high = mid - 1

    return -1



num_list = inputs.random_num_list_generator()

num_list.sort()
print("The list after sorting is :\n",num_list)

key = int(input("\nEnter an element to search : "))  

pos_of_element = binary_search(num_list, key, 0, len(num_list)) # function call for binary search

if pos_of_element != -1:
    print(f"The element {key} is found at position {pos_of_element+1} in sorted array.")
else:
    print(f"The element {key} is not found.")
