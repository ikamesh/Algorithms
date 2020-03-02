import inputs

def recursive_linear_search(num_list, key, low, high):
    if low > high:
        return -1
    elif num_list[low]==key:
        return low
    elif num_list[high]==key:
        return high
    else:
        return recursive_linear_search(num_list, key, low+1, high-1)

num_list = inputs.random_num_list_generator()

key = int(input("Enter the element you want to search : "))


pos_of_key = recursive_linear_search(num_list,key,0,len(num_list))
    
if pos_of_key != -1 :
    print(f"\n\t{key} is at present at position {pos_of_key+1}.\n")
else:
    print(f"\n\t{key} is not present in the list")


