'''NAME: YOGIRAJ PATIL
   PRN NO.:F21113062'''


'''Write a pythonprogram to store first year percentage of students in array. Write function 
for sorting array of floating point numbers in ascending order using 
a) Selection Sort 
b) Bubble sort and display top five scores.'''


n= int(input("enter the number of student in class : "))
print("enter percentage of students ")
percentage=[]
j=1
for i in range (n):
    percent=int(input(f"Student {j}: "))
    percentage.append(percent)
    j+=1  

print("percentage of original list: ")   
for i in range(0, len(percentage)):    
    print(percentage[i], end=" ") 

# Selection sort  
     
temp=0  
for i in range(0, len(percentage)):    
    for j in range(i+1, len(percentage)):    
        if(percentage[i] > percentage[j]):    
            temp = percentage[i]    
            percentage[i] = percentage[j]   
            percentage[j] = temp    
     
print() 
  
print("Percentage of student by selection sort: ")   
for i in range(0, len(percentage)):    
    print(str(percentage[i]), end=" ") 
    
# Bubble sort


def bubbleSort(percentage):
    n = len(percentage)
    
    swapped = False
    
    for i in range(n-1):
       
        for j in range(0, n-i-1):
 
          
            if percentage[j] > percentage[j + 1]:
                swapped = True
                percentage[j], percentage[j + 1] = percentage[j + 1], percentage[j]
         
        if not swapped:
           
            return

bubbleSort(percentage)
print("\n")
print("Percentage of student by bubble sort:")
for i in range(len(percentage)):
    print("% d" % percentage[i], end=" ")

    # top 5 scores
print("\n")
print("TOP 5 SCORES:")
for i in range(n-5,n):
    print(percentage[i], end=" ")