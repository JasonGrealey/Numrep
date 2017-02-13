//
//  MyFileReader.cpp
//  
//  A minimal I/O package to read data from a text file.
//  The text file needs to be a set of (any number of) columns separated by whitespace, eg:
//
//  1.0  0.1 
//  2.0  0.2
//  3.0  0.3
//
//  It is presented to the user in the form of a nxm matrix where 
//    n = number of rows = number of line in file 
//    m = number of columns = number of entries on each line
//
//  The user can also ask for individual columns.
//
//  For use in Numerical Recipes course.
//
//  Created by Grig Cowan/ PeterClarke on 30/07/2013.
//

#include "MyFileReaderArma.h"
#include <stdlib.h>



//......................................
// Constructor
MyFileReader::MyFileReader( std::string filename ):
	m_isValid(false)
{       
	std::vector<double> list;
	std::ifstream file;
	char buffer[256];

	//Open the file if it exists	
	try { file.open(filename.c_str()); }
	catch( int e ) { std::cout << "Exception " << filename << " does not exit - terminating " << std::endl; exit(1); }

	//Read it into the buffer list.
	int nrows=0;	
	int ncols=0;		
	while (!file.eof()) {
		file.getline(buffer, 256);
		if(file.eof()) break;
		nrows++;
		std::string line(buffer);
		std::istringstream line_stream(line);

		//std::cout << "****Row " << nrows << std::endl ;

		ncols=0;		
		while (line_stream) {
			double element;
			line_stream >> element;
			if( !line_stream ) break;
			ncols++;
			//std::cout << " element was " << element << std::endl ;
			list.push_back(element);
		} ;
	}

	
	m_M = new mat( nrows, ncols );
	m_isValid = true ;

	for( int irow=0; irow<nrows; ++irow ) {
		for( int icol=0; icol< ncols; ++icol ) {
			int ind = irow*ncols+icol ;
			(*m_M)(irow,icol) = list[ind] ;
		}
	}

	if ( file != NULL ) file.close();
	
	std::cout << " Read file " << filename << "   which had Ncols= " << ncols << "   nrows= "<<nrows << std::endl;	

}


//Get a column
mat MyFileReader::getColumn( int icol ) {
	if( (icol>=0) && (icol < m_M->n_cols) ) {
		return m_M->col( icol ) ;
	}
	else {
		return mat(0,0);
	}
}


// Print out data set
void MyFileReader::print() {
	if( m_isValid ) {
		std::string msg = "Dataset rows= ";//+Integer.toString(M.getRowDimension())+" / colums = "+Integer.toString(M.getColumnDimension());
		std::cout << msg << std::endl;
		m_M->print();
	}
	else
		std::cout << "Data set is not valid" << std::endl;
}

