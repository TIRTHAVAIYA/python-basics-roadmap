my_dict = {'apple': 3 , 'tirth':1, 'lion':2 , 'surat':55}


sorted_items_by_key = sorted(my_dict.items())

sorted_dict = dict(sorted_items_by_key)

print(f"Original Dictionary : {my_dict}")
print(f"Sorted ny key : {sorted_dict}")