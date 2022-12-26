'''NAME: YOGIRAJ PATIL
   PRN NO.:F21113062'''


''' Write a python program to store roll numbers of student array who attended training
program in sorted order. Write function for searching whether particular student
attended training program or not, using Binary search and Fibonacci search'''



n= int(input("enter the number of student in class : "))
print("enter the roll no. of students ")
roll=[]
j=1
for i in range (n):
    rollno=int(input(f"Student {j}: "))
    roll.append(rollno)
    j+=1
roll.sort()
print(roll)

stud=int(input("Enter roll no. of student that you want to check :"))

# binary search
'''
def binarySearch(roll, low, high, stud):
    if high >=low:
        mid = (high + low)
        
        if (roll[mid] == stud):
            return mid
        
        elif (roll[mid] > stud):
            return binarySearch(roll , low , mid-1 , stud )

        else:
            return binarySearch(roll , mid+1, high , stud )
    else:
        return 0
    
result = binarySearch(roll, 0, len(roll)-1, stud)   

if result != 0:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
'''

#fibonacci search
   
def fibonaccianSearch(roll, stud, n):
   
    fib2 = 0   
    fib1 = 1  
    fib = fib2 + fib1  

    while (fib < n):
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    offset = -1
 
    while (fib > 1):
       
        i = min(offset+fib2, n-1)
        
        if (roll[i] < stud):
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
     
        elif (roll[i] > stud):
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
 
        else:
            return i
 
    if(fib1 and roll[n-1] == stud):
        return n-1
 
    return -1  

x = fibonaccianSearch(roll, stud, n)
if x>=0:
  print("Found at index:",x)
else:
  print(stud,"isn't present in the array")