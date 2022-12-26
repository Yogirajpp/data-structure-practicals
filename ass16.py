'''NAME: YOGIRAJ PATIL
   PRN NO.:F21113062'''


'''Write a Python program to store first year percentage of students in array. Write
function for sorting array of floating point numbers in ascending order using quick sort
and display top five scores.'''



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

#QUICK SORT

def partition(array, low, high):

  pivot = array[high]
  
  i = low - 1
 
  for j in range(low, high):
    if array[j] <= pivot:
      
      i = i + 1

      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1


def quickSort(array, low, high):
  if low < high:

    p = partition(array, low, high)
    quickSort(array, low, p - 1)
    quickSort(array, p + 1, high)


print("original Array")
print(percentage)

size=len(percentage)

quickSort(percentage,0,size-1)


print('Sorted Array in Ascending Order:')
print(percentage)

# top five score
print("\n")
print("TOP 5 SCORES:")
for i in range(n-5,n):
    print(percentage[i], end=" ")