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



//..........................................
//Simple class to calculate a linear function
class Linear {
	private double m = 0.;
	private double c= 1.;
	
	public Linear( ) {}

	// This methis sets up "m"  and "c" 
	public void setParameters( Matrix in ) {
		if( (in.getRowDimension()!=2) || (in.getColumnDimension()!=1) ) System.out.println( "Linear:setParameters: dimension error" );
		m = in.get(0,0) ;
		c = in.get(1,0) ;
		return ;
	}
	
	// This is the evaluate methind for a single input x value. It returns a single y value.
	public double evaluate( double x ) {
		double y = m*x + c ;
		return y ;
	}	

	// This is the evaluate methind for a vector of input x values (returns a vector of y values)
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

class Chisq {
	
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
		
		//This bit constructs the error matrix and takes its inverse
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
	
}
	
	


//..........................................
// The working code

public final class ChisqTask {
	
	public static final void main(String... aArgs){
		log("Evaluating a chisq");

		MyFileReader theData = new MyFileReader("testData.txt") ;
		if(! theData.isValid() ) log("Could not open file testData.txt" ) ;
				
		Matrix x = theData.getColumn(0) ;
		Matrix y = theData.getColumn(1) ;
		Matrix e = theData.getColumn(2) ;

		x.print(5,3);
		y.print(5,3);
		e.print(5,3);

		
		//Create Chisq object
		Chisq chisq = new Chisq( x, y, e ) ;
		
		
		//Finally form the chisq
		double result = chisq.evaluate() ;
		log( "The final Chisq is "+Double.toString(result)) ;

		
	}
	
	
	private static void log(String aMessage){
		System.out.println(aMessage);
	}
	
}


