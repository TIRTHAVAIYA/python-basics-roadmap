def get_user_input_list():
    input_str = input("Enter elements separated by ',' : ")
    return [x.strip() for x in input_str.split(',') if x.strip()]


def get_user_input_set(name):
    input_str = input(f"enter elements for set {name} separated by commas: ")
    return set(x.strip() for x in input_str.split(',') if x.strip())


### CONVERT LIST TO TUPLE AND TUPLE TO LIST ###

#--- LIST TO TUPLE....

input_list = get_user_input_list()
my_tuple = tuple(input_list)

print(f"\n Original List : {input_list}")
print(f"Converted Tuple : {my_tuple} (Type: {type(my_tuple).__name__})")

#--- TUPLE TO LIST....

my_list_from_tuple = list(my_tuple)
print(f"\n Original Tuple : {my_list_from_tuple}")
print(f"Converted List : {my_list_from_tuple} (Type: {type(my_list_from_tuple).__name__})")



###  MAX & MIN ELEMENT FROM TUPLE.. ###

temp_list = get_user_input_list()
my_tuple = tuple(temp_list)

if my_tuple:
    max_ele = max(my_tuple)
    min_ele = min(my_tuple)

    print(f"\n Your Tuple : {my_tuple}")
    print(f"Maximim element : {max_ele}")
    print(f"Minimum element : {min_ele}")

else:
    print("Tuple is empty.")    



### UNION , INTERSECTION , DIFFERENCE OF SETS ###

set_a = get_user_input_set("A")
set_b = get_user_input_set("B")

##UNION 

union_set = set_a.union(set_b)  ## alternative : set_a | set_b

#intersection

intersection_set = set_a.intersection(set_b) ##  alternative : set_a & set_b

#diffrence

difference_set = set_a.difference(set_b)  ##  alternative : set_a - set_b

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")
print("-" * 30)
print(f"Union (A U B): {union_set}")
print(f"Intersection (A ∩ B): {intersection_set}")
print(f"Difference (A - B): {difference_set}")



### CHECK IF TWO SETS ARE DISJOINT ###

set1 = get_user_input_set("1") 
set2 = get_user_input_set("2") 

is_disjoint = set1.isdisjoint(set2)

print(f"\n Set 1 : {set1}")
print(f"\n Set 2 : {set2}")

if is_disjoint:
    print("Result : TRUE. The two sets are disjoint.")
else:
    print("RESULT: FALSE .The two sets are NOT disjoint.")    