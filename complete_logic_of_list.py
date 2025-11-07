## USER INPUT LIST CODE

def get_user_list():
    input_str = input("Enter elements separated by ',' :")
    
    ## handle non-integer input

    try:
        my_list = [int(x.strip()) for x in input_str.split(',')]
        return my_list
    except ValueError:
        print("INVALID INPUT")
        return []
    

### MIN-MAX LOGIC ###

my_list = get_user_list()

if my_list:
    current_max=my_list[0]
    current_min=my_list[0]

    for num in my_list[1:]:
        if num>current_max:
            current_max=num
        if num<current_min:
            current_min=num    

    print(f"\n Your List : {my_list}")
    print(f"Maximum Number : {current_max}")   
    print(f"Minimum Number : {current_min}")   



### REVERSE A LIST ###

reversed_list = []

for i in range(len(my_list)-1,-1,-1):
    reversed_list.append(my_list[i])

print(f"\n Original List: {my_list}")
print(f"Reversed List: {reversed_list}")


### SORTING A LIST ###

n = len(my_list)

# bubble sort

for i in range (n):
    for j in range (0,n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j],my_list[j+1] = my_list[j+1] , my_list[j]

print(f"\n Sorted List : {my_list}")   


### COUNT OCCURRENCES IN A LIST ###

if my_list:
    target = int(input("Enter a number you want to count :"))
    count =0


    for element in my_list:
        if element == target:
            count +=1

    print(f"\n Your List : {my_list}")
    print(f"The number {target} occurs {count} times.")        


### REMOVE DUPLICATES FROM LIST ###

unique_list=[]

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print(f"\n Original List: {my_list}")           
print(f"List without Duplicates: {unique_list}")


### FIND COMMOM ELEMENTS IN 2 LISTS ###

print ("---List-1 Input ---")
list_1 = get_user_list()
print ("---List-2 Input ---")
list_2 = get_user_list()

common_elements = []

for element in list_1:
    if element in list_2:
       if element not in common_elements:
           common_elements.append(element)        

print(f"Commom elements : {common_elements}")         


### ROTATE A LIST FROM K POSITION ###

if my_list:
    try:
        k = int(input("enter the number of postion(k) to rotate right: "))
    except ValueError:
        print("invalid value of k.")    
        k=0

    k = k % len(my_list)

    #rotate using slicing....

    rotated_list = my_list[-k:] + my_list[:-k]
    print(f"\n Original list: {my_list}")
    print(f"Roated list : {rotated_list}")        



