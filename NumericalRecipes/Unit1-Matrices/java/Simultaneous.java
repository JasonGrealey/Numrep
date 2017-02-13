//
//  Chisq.java
//  
//  Final task in Martrices unit
//
//  1. Solve some linear simultaneous equations
//  2. Get eigenvectors of a matrix
//
//  Created by PeterClarke on 25/06/2013.
//

import Jama.*;
	

//..........................................
// The working code

public final class Simultaneous {
	
	public static final void main(String... aArgs){
		log("Final Task - simultaneous equations");

		MyFileReader theMatrix = new MyFileReader("SimultaneousMatrix.txt") ;
		if(! theMatrix.isValid() ) { log("Could not open finalTaskMatrix.txt" );  } 
		Matrix matrix = theMatrix.getMatrix() ;
		matrix.print(5,3);

		MyFileReader theVector = new MyFileReader("SimultaneousVector.txt") ;
		if(! theVector.isValid() ) { log("Could not open finalTaskVector.txt" ); } 
		Matrix vector = theVector.getMatrix() ;
		vector.print(5,3);
		
		Matrix matinv = matrix.inverse() ;
		
		Matrix result  = matinv.times(vector) ;
		
		log(" The solution of the simultaneous equations is " ) ;
		result.print(5,3);
		
	}
	
	
	private static void log(String aMessage){
		System.out.println(aMessage);
	}
	
}


