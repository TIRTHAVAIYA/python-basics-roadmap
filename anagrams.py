str1 = input("Enter a string-1 : ")
str2 = input("Enter a string-2 : ")

def are_anagrams(s1,s2):
    clean_s1 = s1.replace(" ","").lower()
    clean_s2 = s2.replace(" ","").lower()

    ## both string have to be same length
    if len(clean_s1) != len(clean_s2):
        return False
    
    return sorted(clean_s1) == sorted(clean_s2)

print(f"'{str1}' and '{str2}' are anagrams: {are_anagrams(str1,str2)}")

