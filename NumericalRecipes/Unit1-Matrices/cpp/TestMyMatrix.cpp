//
//  main.cpp
//  
//
//  Created by Greig Cowan on 18/09/2013.
//  Copyright 2013 __MyCompanyName__. All rights reserved.
//

#include "MyMatrix.h"
#include <iostream>
#include <MyFileReader.h>
//#include <armadillo>

int main()
{
	std::cout << "TestingMyMatix " << std::endl;

	/*
	// First bit just performs simple tests using hardwired numbers
	MyMatrix A( 3, 5 );
	for( int i=0; i<3;++i ) {
		for(  int j=0; j<5; ++j ) {
			A.setElement(i,j, 10*i+j ) ;
		}
	}
		
	MyMatrix B( 3, 5 ) ;
	for( int i=0; i<3;++i ) {
		for(  int j=0; j<5; ++j ) {
			B.setElement(i,j, 10*i+j+1 ) ;
		}
	}
	
	MyMatrix Z( 5, 3 ) ;
	for( int i=0; i<5;++i ) {
		for(  int j=0; j<3; ++j ) {
			Z.setElement(i,j, 10*i+j+1 ) ;
		}
	}
		
	MyMatrix C(A.add(B));
	MyMatrix D(A.postMultiply(Z));
		
	if ( C.rows() == 0 && C.columns() == 0 )
	{
		std::cout << "Illegal operation" << std::endl;
	}
	else
	{
		std::cout << "A" << std::endl;
		A.printIt();
		std::cout << "B" << std::endl;
		B.printIt();
		std::cout << "Z" << std::endl;
		Z.printIt();
		std::cout << "C" << std::endl;
		C.printIt();
		std::cout << "D" << std::endl;
		D.printIt();
	}
*/
	
	
	// This next bit reads in data from a file using the MyFileReader utility
	
	// Instantiate file reader with relevant input file
	MyFileReader theData("testfile.txt");
	//theData.print();
	
	// Get each column out
	MyMatrix x = theData.getColumn(0) ;
	std::cout << "x values are : " <<std::endl;
	x.printIt() ;
	
	MyMatrix y = theData.getColumn(1) ;
	std::cout << "y values are : " <<std::endl;
	y.printIt() ;
	
	MyMatrix e = theData.getColumn(2) ; 
	std::cout << "errors are : " <<std::endl;
	e.printIt() ;
	

	return 1;
}
	

