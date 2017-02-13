//
//  main.cpp
//  
//
//  Created by Greig Cowan on 18/09/2013.
//  Copyright 2013 __MyCompanyName__. All rights reserved.
//

#include <iostream>
//#include <MyFileReader.h>

#include <stdlib.h>


//#include "gsl.hpp"
#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>


using namespace std;

//......
// This code wraps the raw gsl calls 
namespace gsl {
    
    // default Mersenne Twister using mt19937 algorithm
    static gsl_rng *gslcpp_rng = gsl_rng_alloc(gsl_rng_default);
    
    static double ran_uniform()        // uniform deviate in [0,1)
    {
        return gsl_rng_uniform(gslcpp_rng);
    }
    
    static double ran_gaussian(double sigma=1.0)    // Gaussian deviate
    {
        return gsl_ran_gaussian(gslcpp_rng, sigma);
    }
    
} /* namespace gsl */




int main()
{
	std::cout << "Testing Random number generation in C++ " << std::endl;

	
    // Use rand()    
    // rand() returns an integer between 0 and RAND_MAX
    
    cout << endl << "Testing rand() " << endl ;
    for( int i=0; i<100; ++i ){
        
        double r = (double) rand() /  (double) RAND_MAX ;
        cout << "    "  << r << endl ;
    }
    
  
    // Use GSL wrappers
    
    cout << endl << "Testing gsl wrappers for uniform " << endl ;
    for( int i=0; i<100; ++i ){
        
        double r = gsl::ran_uniform() ;
        cout << "    "  << r << endl ;
    }
    
    cout << endl << "Testing gsl wrappers for gaussian " << endl ;
    for( int i=0; i<100; ++i ){
        
        double r = gsl::ran_gaussian() ;
        cout << "    "  << r << endl ;
    }
    
    
    
	return 1;
}
	

