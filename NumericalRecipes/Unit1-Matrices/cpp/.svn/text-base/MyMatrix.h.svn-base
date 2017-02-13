#ifndef MyMatrix_H
#define MyMatrix_H

#include <vector>

class MyMatrix
{
	public:
		MyMatrix( int, int );
		MyMatrix( const MyMatrix &source );
		~MyMatrix();
		void setElement( int, int, double );
		double getElement( int, int );
		MyMatrix getColumn( int ) ;
		void printIt();
		MyMatrix add( MyMatrix );
		MyMatrix postMultiply( MyMatrix );
		int rows();	
		int columns();	
	private:
		bool checkIndices(int, int);	
		const int m_rows;
		const int m_columns;
		std::vector< std::vector<double> > m_data;
};

#endif
