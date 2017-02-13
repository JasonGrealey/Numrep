//
//  main.cpp
//  
//
//  Created by Greig Cowan on 18/09/2013.
//  Copyright 2013 __MyCompanyName__. All rights reserved.
//

#include <iostream>
//#include <MyFileReader.h>
#include <armadillo>

using namespace arma;
using namespace std;

int main()
{
	std::cout << "Testing Armadillo Matrix package " << std::endl;

	
	// Make and print some matrices
	mat A( 3, 5 );
	for( int i=0; i<3;++i ) {
		for(  int j=0; j<5; ++j ) {
			A(i,j) =  10*i+j  ;
		}  
	}
		
	mat B( 3, 5 ) ;
	for( int i=0; i<3;++i ) {
		for(  int j=0; j<5; ++j ) {
			B(i,j) = 10*i+j+1 ;
		}
	}
	
	mat C( 5, 3 ) ;
	for( int i=0; i<5;++i ) {
		for(  int j=0; j<3; ++j ) {
			C(i,j) = 10*i+j+1  ;
		}
	}
	A.print("A matrix is : ");
	B.print("B matrix is : ");
	C.print("Z matrix is : ");
	
	
	// Add two matrices
	// Note that ti cleverly deals with not knowing the sizes.
	mat D ;
	D = A+B ;
	D.print("D = A+B : ") ;
	
	
	//Multiply two matrices
	mat E;
	E = A*C ;
	E.print("E = A*B : ") ;
	
	//INvert a matrix
	mat F = zeros<mat>(3,3) ;
	mat G ;
	F(0,0) = 0.5 ;
	F(1,1) = 0.33 ;
	F(2,2) = 0.25 ;
	G = F.i();
	F.print("F : ") ;
	G.print("G is inverse of F : ") ;
	

	return 1;
}
	

