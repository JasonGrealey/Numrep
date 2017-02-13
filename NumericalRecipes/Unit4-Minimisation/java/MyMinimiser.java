//
//  MyMinimiser.java
//  
//
//  Created by PeterClarke on 25/06/2013.
//  Copyright 2013 __MyCompanyName__. All rights reserved.
//

import Jama.*;


public class MyMinimiser implements IMinimiser {

	private int numberOfParameters=0 ;
	private int currentParameter = 0; 
	
	private double convergenceLimit= 0.001;
	
	private int maxIterations = 1000000 ;
	private int currentIterations = 0;

	private int minCycles = 100 ;
	private int currentCycles = 0 ;
	
	private boolean isFinished = false ;

	private Matrix parameters ;
	private Matrix increments ;
	
	private double last_chisq = 100000000000. ;	
	
	public void setStartParameters( Matrix params, Matrix incs ) {
		//Check this is a 1D matrix being used as a Vector
		if( params.getColumnDimension() != 1 ) return ;
		numberOfParameters = params.getRowDimension() ;
		parameters = params ;
		increments = incs ;
	}
		
	public void setConvergenceLimit( double conv ) { convergenceLimit = conv ; }

	public void setMaxIterations( int max ) { maxIterations = max; }
	
	public boolean isFinished() { return isFinished ; }
	
	
	// Main minimising method
	public Matrix minimise( double chisq ) {
		
		currentIterations++ ;
		if(currentIterations > maxIterations ) {
			isFinished = true ;
			log("Finished without convergence");
			return parameters ;
			
		}
		
		log("----------");
		log("---chisq= "+Double.toString(chisq)+"   lastchisq= "+Double.toString(last_chisq));
		log("-------m= "+Double.toString(parameters.get(0,0))+"   inc= "+Double.toString(increments.get(0,0)));
		log("-------c= "+Double.toString(parameters.get(1,0))+"   inc= "+Double.toString(increments.get(1,0)));
		
		//Vary parameter being minimised on or move to next parameter
		if( (chisq<last_chisq) && ((last_chisq - chisq) < convergenceLimit) ) {
			//It has converged in this parameter so we move to the next parameter
			currentParameter++ ;
			if( currentParameter > numberOfParameters-1 ) {
				currentParameter = 0 ;
				currentCycles++ ;
				if( currentCycles > minCycles ) {
					isFinished =  true ;
					return parameters ;
				}
			}
			parameters.set(currentParameter,0, parameters.get(currentParameter,0) + increments.get(currentParameter,0) ) ;
			last_chisq = chisq ;
			return parameters ;
			
		}
		else {
			//We continue with this parameter
			if( chisq < last_chisq ) {
				//Continue in same direction
				parameters.set(currentParameter,0, parameters.get(currentParameter,0) + increments.get(currentParameter,0) ) ;
				last_chisq = chisq ;
				return parameters;
			}
			else {
				//Reverse and halve the increment
				increments.set(currentParameter,0, increments.get(currentParameter,0)*-0.6 );
				parameters.set(currentParameter,0, parameters.get(currentParameter,0) + increments.get(currentParameter,0) ) ;
				last_chisq = chisq ;
				return parameters;
			}
		}
	}

	private static void log(String aMessage){
		System.out.println(aMessage);
	}
	
}


