from numpy import matrix

#Create 2 matrices
A = matrix([[1, 1, 0],[1, 0, 1], [1, 0, 0]])
B = matrix([[1, 0, 0],[1, 1, 1], [1, 0, 1]])

print "\n A = "
print(str(A) )


print( "\n B = ")
print(str(B) )


#Add two matrices

C = A + B
print( "\n A + B = ")
print(str(C))


#Add two matrices

C = A * B
print( "\n A * B = ")
print(str(C))


