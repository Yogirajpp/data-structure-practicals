'''NAME: YOGIRAJ PATIL
   PRN NO.:F21113062'''

'''Write a python program to compute following computation on matrix:
a) Addition of two matrices
b) Subtraction of two matrices
c) Multiplication of two matrices
d) Transpose of a matrix'''




# Matrix 1

    
numba=[]

numb1=[]
n = 3
print("Enter the value of row in column1",n," :")
for i in range(0, n):
    x = int(input(f"enter {i+1} number:"))
    numb1.append(x)
    
    
numb2=[]
n = 3
print("Enter the value of row in column2",n," :")
for i in range(0, n):
    x = int(input(f"enter {i+3+1} number:"))
    numb2.append(x)


numb3=[]
n = 3
print("Enter the value of row in column3",n," :")
for i in range(0, n):
    x = int(input(f"enter {i+3+3+1} number:"))
    numb3.append(x)
        
numba=[numb1,numb2,numb3]
print(" matrix first " + str(numba))


# Matrix 2



    
numbb=[]
numb4 =[]

n = 3
print("Enter the value of row in column1",n," :")
for i in range(0, n):
    x = int(input(f"enter {i +1} number:"))
    numb4.append(x)

numb5=[]
n = 3
print("Enter the value of row in column2",n," :")
for i in range(0, n):
    x = int(input(f"enter {i+3+1} number:"))
    numb5.append(x)


numb6=[]
n = 3
print("Enter the value of row in column3",n," :")
for i in range(0, n):
    x = int(input(f"enter {i+3+3+1} number:"))
    numb6.append(x)
    
numbb=[numb4,numb5,numb6]
print(" matrix second "+ str(numbb))


result= [[0,0,0],[0,0,0],[0,0,0]]

# Addition of two matrices


# through rows
print("\n")
print("Addition of two matrices\n")
for i in range(len(numba)):
    #through columns
    for j in range(len(numba[0])):
        result[i][j] = numba[i][j] + numbb[i][j]
        
for r in result:
    print(r)

# Substraction of two matrices  

# through rows 
print("\n")
print("substraction of two matrices\n")
for i in range(len(numba)):
    #through columns
    for j in range(len(numba[0])):
        result[i][j] = numba[i][j] - numbb[i][j]
        
for r in result:
    print(r)

# Multiplication of two matrices
print("\n")
print("Multiplication of two matrices\n")
#through rows
for i in range(len(numba)):
    #through columns
    for j in range(len(numbb[0])):
        #through rows
        for k in range(len(numbb[0])):
             result[i][j] += numba[i][k] * numbb[k][j]
        
for r in result:
    print(r)


#Transpose of a first matrix
print("\n")
print("Transpose of a first matrix\n")
for i in range(len(numba)):
    #through columns
    for j in range(len(numba[0])):
        result[i][j] = numba[j][i] 
        
for r in result:
    print(r)

#Transpose of a second matrix
print("\n")
print("Transpose of a second matrix\n")
for i in range(len(numbb)):
    #through columns
    for j in range(len(numbb[0])):
        result[i][j] = numbb[j][i] 
        
for r in result:
    print(r)







