import inputs

def binary_search(num_list, key, low, high):

    while low <= high:
        mid = low + (high-low)//2
        print(mid)
        if num_list[mid]==key:
            return mid
        
        elif num_list[mid]<=key:
            low = mid+1
        
        else:
            high = mid-1

    return -1



num_list = inputs.random_num_list_generator()
num_list.sort()
print("Sorted array is :\n",num_list)

key = int(input("\nEnter an element to search : "))

pos_of_element = binary_search(num_list, key, 0, len(num_list))

if pos_of_element != -1:
    print(f"The element {key} is found at position {pos_of_element+1} in sorted array.")
else:
    print(f"The element {key} is not found.")
