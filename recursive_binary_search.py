import inputs

def recusive_binary_search(num_list, key, low, high):
    if low>=high:
        return -1

    mid = low+(high-low)//2
     
    if num_list[mid]==key:
        return mid
    elif num_list[mid]>key:
        return recusive_binary_search(num_list, key, mid+1, high)
    else:
        return recusive_binary_search(num_list, key, low, mid-1)

num_list = inputs.random_num_list_generator()
key = int(input("\nEnter the number you want to find :"))
num_list.sort()

pos_of_element = recusive_binary_search(num_list, key, 0, len(num_list))

if pos_of_element!=1:
    print(f"{key} is present in list at position {pos_of_element+1}")
else:
    print(f"{key} is not present in the list.")

