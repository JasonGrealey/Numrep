//
//  TestMyFileReader.cpp
//
//  To demonstrate how ot use the MyFileReader.cpp utility

#include "MyFileReader.h"

int main()
{

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

