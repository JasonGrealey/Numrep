//
//  Chisq.java
//  
// Exercise to form a chisq from a set of dat points and a theoretical line 
// This is an exercise in Unit 1 of the course.
//
// This is essentially the same as Chisq, but it is recast to put the work int a Chisq class.
// This is done in anticipation of needing to do this for the next unit on minimisation.
//
//  Created by PeterClarke on 25/06/2013.
//

import Jama.*;
//import org.freehep.math.minuit.FCNBase;
import org.freehep.math.minuit.*;

//..........................................
//Simple class to calculate a linear function
class Linear {
	private double m = 0.;
	private double c= 1.;
	
	public Linear( ) {}

	public void setParameters( Matrix in ) {
		if( (in.getRowDimension()!=2) || (in.getColumnDimension()!=1) ) System.out.println( "Linear:setParameters: dimension error" );
		m = in.get(0,0) ;
		c = in.get(1,0) ;
		return ;
	}
	
	public double evaluate( double x ) {
		return m*x + c ;
	}	

	public Matrix evaluate( Matrix x ) {
		int length = x.getRowDimension();
		
		Matrix result = new Matrix(length,1) ;
		for(int ind=0;ind<length;++ind) {
			result.set(ind,0, m*x.get(ind,0)+c ) ;
		}
		return result ;
	}	
}
	


//......................................
// Class to provide a method to calcualte chisq

class Chisq implements FCNBase {
	
	private Linear func = new Linear() ;
	private Matrix x;
	private Matrix y;
	private Matrix IE ;
	
	//...................................
	// This is the constructor which sets up the constant vectors (data x and y) and matrices (inverse error matrix)
	// These never change in the calculation
	public Chisq( Matrix xin, Matrix yin, Matrix ein ) {
		
		//Do some checks 
		boolean valid =  
			(xin.getRowDimension() == yin.getRowDimension()) &&
			(yin.getRowDimension() == ein.getRowDimension()) &&
			(xin.getColumnDimension() == 1) &&
			(yin.getColumnDimension() == 1) &&
			(ein.getColumnDimension() == 1) ;
		
		if( ! valid )  System.out.println("input x-y-e dimension error") ;
		
		x = xin.copy() ;
		y = yin.copy() ;
		
		Matrix D = new Matrix( ein.getRowDimension(), ein.getRowDimension() );
		for(int ind=0; ind < ein.getRowDimension(); ++ind ) {
			D.set(ind,ind,ein.get(ind,0)*ein.get(ind,0)) ;
		}
		IE = D.inverse() ;
	}
	
	//........................
	// To pass in a new set of parsmeters, in this case m & c
	public void setParameters( Matrix params ) {
		func.setParameters( params ) ;
	}
	
	
	//........................
	// Evaluate the chisq
	public double evaluate( ) {
	
		// Create a vector of theoretical points
		Matrix yth = func.evaluate( x ) ;
		//yth.print(5,3) ;
		
		//Take difference		
		Matrix D ;
		D = y.minus( yth) ;
		//D.print(5,3) ;
		
		//Finally form the chisq
		Matrix DT = D.transpose() ;
		Matrix CHISQ = DT.times( IE.times(D) ) ;
		//CHISQ.print(5,3);
		return CHISQ.get(0,0) ;
	}
	
    //.......................
    // Extra method needed for the interface FCNbase
	public double valueOf( double[] par ) {
		Matrix params = new Matrix(2,1) ;
		params.set(0,0, par[0] );
		params.set(1,0, par[1] ) ;
		setParameters( params ) ;
		return evaluate() ;
	}
		
	
}
	
	


//..........................................
// The working code

public final class MinuitFit {
	
	public static final void main(String... aArgs){

		log("***********************");
		log("Perfoming a simple fit");

		log("    Read in data");

		//MyFileReader theData = new MyFileReader("testData.txt") ;
		MyFileReader theData = new MyFileReader("testDataII.txt") ;  // more interesting data
		if(! theData.isValid() ) log("Could not open file testData.txt" ) ;
				
		Matrix x = theData.getColumn(0) ;
		Matrix y = theData.getColumn(1) ;
		Matrix e = theData.getColumn(2) ;

		x.print(5,3);
		y.print(5,3);
		e.print(5,3);

		
		log("    Calculate chisq initially");

		
		//Create Chisq object
		Chisq chisq = new Chisq( x, y, e ) ;
		
		
		//Initial chisq
		double result = chisq.evaluate() ;
		log( "The initial Chisq is "+Double.toString(result)) ;

		
		//Set up to do minimisation
		log("    Create a minimiser");
		
		//Set up parameters
		MnUserParameters upar = new MnUserParameters();
		upar.add("m", 0., 0.1);
		upar.add("c", 1., 0.1);
		
        //Create minimiser
		MnMigrad migrad = new MnMigrad(chisq, upar);

        // Do the minimisation -- all the work is done here
		FunctionMinimum min = migrad.minimize();
        
        // Report results
		System.out.println("minimum: "+min);
		

		
	}
	
	
	private static void log(String aMessage){
		System.out.println(aMessage);
	}
	
}


