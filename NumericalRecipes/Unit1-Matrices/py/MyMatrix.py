class Matrix:

    matrix = [[]]

    #............................
    #Constructors
    def __init__(self, m, n):
        self.rows = m   #number of rows
        self.cols = n   #number of columns
        self.matrix = [[0 for j in range(n)] for i in range(m)]


    def set_matrix(self, data):
        if self.rows == len(data) and self.cols == len(data[0]) :
            self.matrix = data
        else:
            print("Error - you tried to set_Matrix with an operand of wrong dimensions")


    #............................
    #Primitive access methods
    def set_element(self, i, j, element):
        self.matrix[i][j] = element
    
    def get_element(self, i, j):
        return self.matrix[i][j]
    
    def get_rows(self):
        return self.rows
    
    def get_cols(self):
        return self.cols
    
    def checkDimension( self, operand):
        if self.rows==operand.get_rows() and self.cols==operand.get_cols() : return True
        else:  return False
    


    #............................
    #Add methods

    def __add__( self, operand ):
        return self.add(operand)
    

    def add(self, operand):
 
        # check that the matrices are the same size
        if self.checkDimension(operand):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.set_element(i, j, self.get_element(i, j) + operand.get_element(i, j))
            return result
        
        # otherwise raise an error that they are off different size
        else:
            print("Error - matrices are different dimensions")
            return 0



    #............................
    #Add post multiply methods


    def __mul__(self, operand):
        return self.postMultiply(operand)
        
    def postMultiply(self, operand):
   
        #Check dimensions match for multiplication
        if self.cols == operand.get_rows():
            result = Matrix(self.rows, operand.get_cols())
            for i in range(self.rows):
                for j in range(operand.get_cols()):
                    element = 0
                    for k in range(self.cols):
                        element += self.get_element(i, k) * operand.get_element(k, j)
                        result.set_element(i, j, element)
            return result

        else:
            print("Error - matrices are wrong dimensions for multiplication")
            return 0



    #............................
    #Print method
    def __str__(self):
        for i in range(self.get_rows()):
            print( str(self.matrix[i]) )
        return " "
