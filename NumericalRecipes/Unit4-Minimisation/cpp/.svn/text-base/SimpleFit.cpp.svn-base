//
// Chisq.cpp
//  
// Exercise to form a chisq from a set of dat points and a theoretical line 
// This is an exercise in Unit 1 of the course.
//
// This is essentially the same as Chisq, but it is recast to put the work int a Chisq class.
// This is done in anticipation of needing to do this for the next unit on minimisation.
//
// Created by Greig Cowan on 18/09/2013.
//

#include <iostream>
#include <string>
#include <sstream>
#include "../../Unit1-Matrices/cpp/MyMatrix.h"
#include "MyMinimiser.h"
#include "MyFileReader.h"

//Simple class to calculate a linear function
class Linear {
	private:
		double m;
		double c;

	public:
		Linear() { m = 1.; c = 0.;}

		void setParameters( MyMatrix in ) {
			if( (in.getRowDimension()!=2) || (in.getColumnDimension()!=1) ) log( "Linear:setParameters: dimension error" );
			m = in.get(0,0) ;
			c = in.get(1,0) ;
			return ;
		}

		double evaluate( double x ) {
			return m*x + c ;
		}	

		MyMatrix evaluate( MyMatrix x ) {
			int length = x.getRowDimension();

			MyMatrix result(length,1) ;
			for(int ind=0;ind<length;++ind) {
				result.set(ind,0, m*x.get(ind,0)+c ) ;
			}	
			return result ;
		}	
};

// Class to provide a method to calcualte chisq
class Chisq {

	private:
		Linear func() ;
		MyMatrix x;
		MyMatrix y;
		MyMatrix IE ;

		// This is the constructor which sets up the constant vectors (data x and y) and matrices (inverse error matrix)
		// These never change in the calculation
	public:
		Chisq( MyMatrix xin, MyMatrix yin, MyMatrix ein ) {

			//Do some checks 
			bool valid =  
				(xin.getRowDimension() == yin.getRowDimension()) &&
				(yin.getRowDimension() == ein.getRowDimension()) &&
				(xin.getColumnDimension() == 1) &&
				(yin.getColumnDimension() == 1) &&
				(ein.getColumnDimension() == 1) ;

			if( ! valid ) log("input x-y-e dimension error") ;

			x = xin.copy() ;
			y = yin.copy() ;

			MyMatrix D( ein.getRowDimension(), ein.getRowDimension() );
			for(int ind=0; ind < ein.getRowDimension(); ++ind ) {
				D.set(ind,ind,ein.get(ind,0)*ein.get(ind,0)) ;
			}
			IE = D.inverse() ;
		}

		// To pass in a new set of parsmeters, in this case m & c
		void setParameters( MyMatrix params ) {
			func.setParameters( params ) ;
		}


		// Evaluate the chisq
		double evaluate( ) {

			// Create a vector of theoretical points
			MyMatrix yth = func.evaluate( x ) ;
			//yth.print(5,3) ;

			//Take difference		
			MyMatrix D ;
			D = y.minus( yth) ;
			//D.print(5,3) ;

			//Finally form the chisq
			MyMatrix DT = D.transpose() ;
			MyMatrix CHISQ = DT.times( IE.times(D) ) ;
			//CHISQ.print(5,3);
			return CHISQ.get(0,0) ;
		}

};

// The working code
int main()
{

	log("***********************");
	log("Perfoming a simple fit");

	log("    Read in data");

	MyFileReader theData = new MyFileReader("testDataII.txt") ;
	if(! theData.isValid() ) log("Could not open file testDataII.txt" ) ;
	log("here");

	MyMatrix x = theData.getColumn(0) ;
	MyMatrix y = theData.getColumn(1) ;
	MyMatrix e = theData.getColumn(2) ;

	x.print(5,3);
	y.print(5,3);
	e.print(5,3);


	log("    Calculate chisq initially");


	//Create Chisq object
	Chisq chisq( x, y, e ) ;


	//Finally form the chisq
	double result = chisq.evaluate() ;
	log( "The initial Chisq is ");//+Double.toString(result)) ;


	//Set up to do minimisation
	log("    Create a minimiser");

	//Set up
	MyMinimiser minim() ;

	MyMatrix params(2,1) ;
	MyMatrix incs(2,1) ;
	params.set(0,0, 0. );
	params.set(1,0, 1. ) ;
	incs.set(0,0,0.01 ) ;
	incs.set(1,0,0.01) ;

	minim.setStartParameters( params, incs ) ;


	//Minimise in loop; until its finished

	log("    Running minimisation");

	while( ! minim.isFinished() ) {
		chisq.setParameters( params ) ;
		params = minim.minimise( chisq.evaluate( ) ) ;
	}

	log("    Minimisation converged");
	//log("        final chisq is: "+Double.toString(chisq.evaluate( )));
	log("        parameters are: " );
	params.print(5,3) ;
	return 1;
}

