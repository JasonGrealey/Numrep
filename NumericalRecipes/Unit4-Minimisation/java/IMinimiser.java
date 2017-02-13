//
//  IMinimiser.java
//  
//
//  Created by PeterClarke on 28/Aug/2013.
//  Copyright 2013 __MyCompanyName__. All rights reserved.
//


import Jama.*;


public interface IMinimiser {
	
	// To set convergence criteria
	public void setConvergenceLimit( double conv) ;
	public void setMaxIterations( int max ) ;
	public void setStartParameters( Matrix params, Matrix incs ) ;
	
	// Main minimising method
	public Matrix minimise( double chisq ) ;
	
	//Methods to report if finished
	public boolean isFinished() ;
	
	// At the end you will need to know the errors.
	//public Matrix getErrors() 
	
}