'''NAME: YOGIRAJ PATIL
   PRN NO.:F21113062'''


'''Write a python program to store roll numbers of student in array who attended
training program in random order. Write function for searching whether particular
student attended training program or not, using Linear search and Sentinel search.'''


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
# linear search
def linearSearch(stud):

    for i in range(n):
        if stud==(int(roll[i])):
            return i
    else:
        return "no such student found"


print("if it show '1' then the respective student attended the training program:",linearSearch(stud))

# sentine search

def sentineSearch(roll,rollno,stud):
    last=roll[n-1]
    roll[n-1] = stud
    i=0

    while(roll[i]!=stud):
        i+=1

    roll[n-1]=last

    if((i<n-1) or (roll[n-1]==stud)):
        return i
    else:
        return "no such student found"

print("if it show '1' then the respective student attended the training program: ",sentineSearch(roll,rollno,stud))


