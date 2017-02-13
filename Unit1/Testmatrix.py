from matrix import *

#Create 2 matrices
A = Matrix(3,3)
B = Matrix(3,3)

#Fill the matrices.
A.__setitem__([[1, 1, 0],[1, 0, 1], [1, 0, 0]])
B.__setitem__([[1, 0, 0],[1, 1, 1], [1, 0, 1]])

print "A = "
print(str(A) )
print( "B = ")
print(str(B) )
		
#Add two matrices using both methods

C1 = A.__add__(B)
print( "A + B = ")
print(str(C1))

C2 = A + B
print( "A + B = ")
print(str(C1))


#Add two matrices using both methods
C1 = A.__mul__(B)
print( "A * B = ")
print(str(C1))
	
C2 = A * B
print( "A * B = ")
print(str(C2))
    
