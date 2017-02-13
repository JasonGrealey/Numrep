//
//  TestMyMatrix.java
//  
//
//  Created by PeterClarke on 25/06/2013.
//  Copyright 2013 __MyCompanyName__. All rights reserved.
//

//import java.util.Random;
import Jama.*;

//To use and test the Jama matrix algebra package

public final class TestJama {
	
	public static final void main(String... aArgs){
		log("Testing Jama ");
		
		
	    // Creating and adding matrices
		Matrix A = new Matrix( 3, 5 );
		for( int i=0; i<3;++i ) {
			for(  int j=0; j<5; ++j ) {
				A.set(i,j, 10*i+j ) ;
			}
		}

		
		Matrix B = new Matrix( 3, 5) ;
		for( int i=0; i<3;++i ) {
			for(  int j=0; j<5; ++j ) {
				B.set(i,j, 10*i+j+1 ) ;
			}
		}
		
		Matrix C ;
		
		C = A.plus(B) ;
		
		if ( C == null ) log( "Illegal operation" ) ;
		else {
			log("A");
			A.print(5,3);
			log("B");
			B.print(5,3);
			log("C");
			C.print(5,3);
		}
		

		//Inverting a matrix
		
		Matrix E = new Matrix(3,3) ;
		E.set(0,0, 0.5);
		E.set(1,1,0.2) ;
		E.set(2,2,0.4);
		
		Matrix I = E.inverse() ;
		
		log( "" );
		log(" Inverting E " );
		I.print(4,3) ;
		
		
	}
	
	
	private static void log(String aMessage){
		System.out.println(aMessage);
	}
	
}


