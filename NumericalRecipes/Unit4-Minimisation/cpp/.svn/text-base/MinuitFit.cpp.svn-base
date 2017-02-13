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
#include <armadillo>
#include "TMinuit.h"
#include "../../MyUtilities/cpp/MyFileReaderArma.h"


using namespace arma;

//Simple class to calculate a linear function
class Linear {
	private:
		double m;
		double c;

	public:
		Linear() { m = 0.; c = 1.;}

		void setParameters( mat in ) {
			m = in(0,0) ;
			c = in(1,0) ;
			return ;
		}

		double evaluate( double x ) {
			return m*x + c ;
		}	

		mat evaluate( mat x ) {
			int length = x.n_rows;

			mat result(length,1) ;
			for(int ind=0;ind<length;++ind) {
				result(ind,0) = m*x(ind,0)+c  ;
			}
			return result ;
		}	
};

// Class to provide a method to calcualte chisq
class Chisq {

	private:
		Linear func ;
		mat x;
		mat y;
		mat e;
		mat IE ;

		// This is the constructor which sets up the constant vectors (data x and y) and matrices (inverse error matrix)
		// These never change in the calculation
	public:
		Chisq( mat  xin, mat  yin, mat  ein ) : x(xin), y(yin), e(ein) {

			mat D( e.n_rows, e.n_rows );
			D.zeros();
			for(int ind=0; ind < e.n_rows; ++ind ) {
				D(ind,ind) = e(ind,0)*e(ind,0) ;
			}
			IE = D.i() ;
		}

		// To pass in a new set of parsmeters, in this case m & c
		void setParameters( mat params ) {
			func.setParameters( params ) ;
		}


		// Evaluate the chisq
		double evaluate(  ) {

			// Create a vector of theoretical points
			mat yth = func.evaluate( x ) ;
			//yth.print(5,3) ;

			//Take difference
			mat D ;
			D = y - yth ;

			//Finally form the chisq
			mat DT = D.t() ;
			mat CHISQ = DT * IE * D ;
			//CHISQ.print(5,3);
			return CHISQ(0,0) ;
		}


};


//........................
// need object in global namespace
Chisq * theChisqObject = 0 ;

// Minuit function interface
//void fcn(int& npar, double* deriv, double& f, double par[], int flag) {
void fcn(Int_t& npar, Double_t* deriv, Double_t& f, Double_t par[], Int_t flag) {
	mat p(2,1);
	p(0,0) = par[0];
	p(1,0) = par[1];
	theChisqObject->setParameters( p );
	double result = theChisqObject->evaluate() ;
	std::cout << " In FCN " << p(0,0) << "  "  << p(1,0) << "   resutl " << result << std::endl;
	f= result ;
}



// The working code
int main()
{

	std::cout << "***********************" <<std::endl;
	std::cout << "Perfoming a simple fit"<<std::endl;

	std::cout << "    Read in data"<<std::endl;

	MyFileReader theData("testData.txt");
	if(! theData.isValid() ) std::cout << "Could not open file testData.txt" <<std::endl;

	mat x = theData.getColumn(0) ;
	mat y = theData.getColumn(1) ;
	mat e = theData.getColumn(2) ;

	std::cout << "x matrix: "<<std::endl;
	x.print();
	std::cout << "y matrix: "<<std::endl;
	y.print();
	std::cout << "error matrix: "<<std::endl;
	e.print();

	//Create Chisq object
	Chisq chisq( x, y, e ) ;
	theChisqObject = & chisq ;
	double result = chisq.evaluate( ) ;
	std::cout <<  "The initial Chisq is " << result <<std::endl;//+Double.toString(result)) ;

	//Set up to do minimisation
	std::cout << "    Create a minimiser"<<std::endl;

	TMinuit m_minuit(2);
	m_minuit.SetFCN(fcn);
	m_minuit.SetErrorDef(1.0);
	m_minuit.SetPrintLevel(1); 

	m_minuit.DefineParameter(0, "m", 0., 0.01, -10., 10. ) ;
	m_minuit.DefineParameter(1, "c", 1., 0.01, -10., 10. ) ;


	std::cout << "    Running minimisation"<<std::endl;

	m_minuit.Migrad() ;

	std::cout << "    Minimisation converged"<<std::endl;
	//std::cout << "        final chisq is: "+Double.toString(chisq.evaluate( )));
	std::cout << "        parameters are: " <<std::endl;
	//params.print(5,3) ;
	return 1;
}

