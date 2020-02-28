# import inputs

# num_list = inputs.random_num_list_generator()
# num_list2 = inputs.finite_num_list()
# num_list3 = inputs.infinite_num_list()
# print(num_list3)

num_list = [] 
while True:
    try:
        num = input("Enter num to fill the list : ")
        if type(int(num)) == 'int':
            num_list.append(int(num))
        elif "x" in num.lower() :
            break
        else:
            continue
    except:
        pass

print(num_list)


