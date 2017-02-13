//
//  MyGaussianPdf.java
//  
//
//  Created by PeterClarke on 25/06/2013.
//  Copyright 2013 __MyCompanyName__. All rights reserved.
//

import java.lang.Math;
import java.util.Random;

public class MyGaussianPdf {

    //------------
	//Member variables needed for the class to do its job
	private double mean ;
	private double width ;
	private Random randomGenerator ;
	
	//Constructor 
	public MyGaussianPdf( double m, double w ) {
		mean = m ;
		width = w ;
		randomGenerator = new Random();
	}
	
    
    //------------
	//Method to return value fo Gaussian at point x
	public double evaluate( double x ) {
		double val = Math.exp( -(x-mean)*(x-mean) / 2.0 / width*width ) ;
		return val ;
	}
    

    //------------
	//Method to return the maximum possible value fo the function
	public double max( ) {
		return 1.0 ;
	}
	
    
    //---------------
	//Method to return a random number with a Gaussian distribution in +- 3 sigma
	public double next() {
		
		double test1,test2,test3 ;
		
		do {
			test1 = (randomGenerator.nextDouble() -0.5) * 2.0 ;
			test1 = test1 * width * 3.0 + mean;
			test2 = evaluate( test1);
			test3 = randomGenerator.nextDouble() * max() ;
		} while( test3 > test2 ) ;
		
		return test1 ;
	}
    
    
	//---------------
	//Method to return the numeric integral of the function between lo < x < hi
	public double integralNumeric( double lo, double hi ) {
		

		int npoints = 1000000 ;
		int ninside = 0;
		
		for( int ii=1; ii<=npoints; ++ii ) {
			
			//Generate a random number on the x-axis
			double x = lo + randomGenerator.nextDouble()*(hi-lo) ;
			
			//Generate a random number on the y-axis
			double y = randomGenerator.nextDouble()* max() ;
			
			//Is it inside ?
			if( y < evaluate(x) ) ++ninside ;
		}
		
		double Atot = (hi-lo)*max() ;
		double Ainside = Atot * ninside/npoints ;
		
		return Ainside ;
	}
	
    
    //-----------------
	//Method to return the numeric integral of the function between lo < x < hi
	public double integralNumericII( double lo, double hi ) {
		
        
		int npoints = 1000000 ;
		
        double sumf = 0;
        
		for( int ii=1; ii<=npoints; ++ii ) {
			
			//Generate a random number on the x-axis
			double x = lo + randomGenerator.nextDouble()*(hi-lo) ;
			
			//Calculate and accumulate value of function
			sumf+= evaluate(x) ;
		}
		
		double Area = sumf *(hi-lo) / npoints ;

		return Area ;
	}
	
    
    //--------------
	//Method to return the analytic integral of the function between lo < x < hi
	public double integralAnalytic( double lo, double hi ) {
		
		// For a Gaussian there is a simple formula for its integral
        // This assumed lo=0 anf hi=infinity, actually the proper formula should go in but its hard
		double A = width*Math.sqrt(2.0 * Math.PI  ) ;
		return A ;
	}
	
	
    //------------
	//Fundamental method to return PDF value fo Gaussian at point x
	public double PDF( double x ) {
		double val = Math.exp( -(x-mean)*(x-mean) / 2.0 / width*width ) ;
        double norm = integralAnalytic( 0, 1000 ) ;
		return val/norm ;
	}
    
    
	
	
	
}



