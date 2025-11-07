## RIGHT TRIANGLE STAR PATTERN

n=5 
print("RIGHT TRIANGLE : ")
for i in range(1 , n+1):
    print("*"*i)


## INVERTED RIGHT TRIANGLE STAR PATTERN

print("INVERTED RIGHT TRIANGLE : ")
for i in range (n , 0 , -1):
    print("*"*i)


## FULL PYRAMID

print("FULL PYRAMID : ")
for i in range (1 , n+1):
    spaces = " "*(n-i)
    stars = "*" * (2*i-1)
    print(spaces+stars)

## INVERTED FULL PYRAMID

print("INVERTED FULL PYRAMID : ")
for i in range(n , 0 , -1):
    spaces = " "*(n-i)
    stars = "*" * (2*i-1)
    print(spaces+stars)


## DIAMOND STAR PATTERN
print("DIAMOND STAR : ")

#upper half logic 
for i in range (1,n+1):
    print(" " * (n-i) + "*" * (2*i-1))
#lower half logic 
for i in range (n-1,0,-1):
    print(" " * (n-i) + "*" * (2*i-1))


## HOLLOW SQUARE PATTERN

print("HOLLOW SQUARE PATTERN")

for i in range (n):
    for j in range (n):
        #check if it is border position
        if i==0 or i==n-1 or j ==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" " , end=" ")    
    print()        


## NUMBER PATTERNS
# SIMPLE INCREMENTAL TRIANGLE
print ("SIMPLE INCREMENTAL TRIANGLE")  
for i in range (1 , n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()  


## FLOYD'S TRIANGLE    

num =1 
print ("FLOYD'S TRIANGLE") 
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num , end=" ")
        num +=1
    print()


##ROW NUMBER TRIANGLE
print ("ROW NUMBER TRIANGLE") 
for i in range (1 , n+1):
    print(str(i)*i)