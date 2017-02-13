//
//  MyMatrix.cpp
//  
//
//  Created by Greig Cowan on 18/09/2013.
//  Modified by Peter Clarke 23/09/2013
//
//  Note that in this simple example for early use in the class we have avoided the memory leak risk of returning 
//  pointers to new MyMatrix objects.
//  It is questionable whether you would really do this for several reasons, including the need to know the return matrix
//  dimension in some situations.

#include "MyMatrix.h"
#include <iostream>
#include <sstream>
#include <string>

//.....................................
// Constructor
MyMatrix::MyMatrix( int r, int c ) :
	m_rows(r),
	m_columns(c)
{
    // Create a "vector of vector of doubles".  
	// Vectors are described in the Stadard Template Libray.

	//First an empty row vector
	std::vector<double> row;
	for ( int j = 0; j < m_columns; ++j )
	{
		row.push_back(0.);
	}
	
	//Insert one of these for each row
	for( int i = 0; i < m_rows; ++i )
	{
		m_data.push_back(row);
	}
}

//...........................
// Copy constructor - needed for assignment of return arguments.
MyMatrix::MyMatrix( const MyMatrix &source ) :
	m_rows(source.m_rows),
	m_columns(source.m_columns),
	m_data(source.m_data)
{}


//............................
// Destructor
MyMatrix::~MyMatrix()
{
}

//............................
//Set value of an element
void MyMatrix::setElement( int i, int j, double val )
{
	if( checkIndices( i,j ) )
	{
		m_data[i][j] = val;
	}
}
	
//...............................
//Get value of an element
double MyMatrix::getElement( int i,  int j )
{
	if( checkIndices( i, j ) )
	{
		return m_data[i][j];
	}
	else
	{
		return 0.;
	}
}

//..............................
//Get a column as a 1-D submatrix
MyMatrix MyMatrix::getColumn( int icol)
{	
	
	//Note  - in this code we return a Matrix. 
	// This relies upon the MyMtrix copy constructor
	// This is to avoid pointers and the associalted memory leak risk.
	
	if( checkIndices( 0, icol ) )
	{
		MyMatrix col(m_rows, 1 ) ;
		for( int irow=0; irow<m_rows; irow++ ) {
			col.setElement(irow,0, m_data[irow][icol]);
		}
		return col;
	}
	else
	{
		return MyMatrix(0,0);
	}
}


//.................................
// Print element	
void MyMatrix::printIt()
{
	for( int i = 0; i < m_rows; ++i ) {
		std::string line = " ";
		for(  int j = 0; j < m_columns; ++j )
		{
			std::stringstream ss;
			ss << m_data[i][j];
			line += ss.str() + " ";
		}
		std::cout << line << std::endl;	
	}
}
	
//........................................
//Some Utility methods 
int MyMatrix::rows() { return m_rows; }
int MyMatrix::columns() { return m_columns; }
	

//.........................................
//Add two matrices
MyMatrix MyMatrix::add( MyMatrix A )
{
	if( this->rows() == A.rows() && this->columns() == A.columns() ) {
		MyMatrix R( this->rows(), this->columns() ) ;
		for( int i=0; i<m_rows;++i ) {
			for(  int j=0; j<m_columns; ++j )
			{
				R.setElement(i,j, this->getElement(i,j) + A.getElement(i,j) ) ;
			}
		}
		return R ;
	}
	else return MyMatrix(0,0);
}

//..........................................				
//Multiply two matrices
MyMatrix MyMatrix::postMultiply( MyMatrix A )
{
	if( this->columns() == A.rows() )
	{
		MyMatrix R( this->rows(), A.columns() );	
		for( int i=0; i<this->rows();++i )
		{
			for(  int j=0; j<A.columns(); ++j ) 
			{
				double val=0;
				for( int p=0; p< this->columns(); ++p )
				{ 
					val+= this->getElement( i, p ) * A.getElement( p, j ) ;
				}
				R.setElement(i, j, val);
			}
		}
		return R;
	}
	else return MyMatrix(0,0);
}
	
//............................................
//Common internal check
bool MyMatrix::checkIndices( int i, int j ) 
{
	if( (i>=0) && (i<m_rows) && (j>=0) && (j<m_columns) ) {return true;}
	return false;
}

