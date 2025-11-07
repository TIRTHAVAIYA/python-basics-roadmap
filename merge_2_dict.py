dict1 = {'a':1 , 'b':2, 'c':3}
dict2 = {'c':20 , 'd':55, 'e':5}

dict1_copy = dict1.copy()
dict1_copy.update(dict2)
merged_dict_update = dict1_copy

print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")

print(f"\n Merged Dictionary : {merged_dict_update}")