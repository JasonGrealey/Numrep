# Python matrix class


class Matrix:

        #intialisation Constructor
        def __init__(self,row,column):
            self.row=row
            self.column=column
            self.matrix= [[0 for a in range(column)] for b in range(row)]

        #copy constructor
        def copy(self,matrix):
            self.matrix=matrix

        #setter method
        def __setitem__(self,input):
            self.matrix=input

        #getter method
        def __getitem__(self,i,j):
            return(self.matrix[i][j])
            
        def __add__(self,other):
            return [[(self.matrix[i][j]+other.matrix[i][j]) for j in range(self.column)]for i in range(self.row)]

        def sub(self,other):
             return [[(self.matrix[i][j]-other.matrix[i][j]) for j in range(self.column)]for i in range(self.row)]
        def __mul__(self,other):
             return [[(self.matrix[i][j]*other.matrix[j][i]) for j in range(self.column)]for i in range(self.row)]

            
