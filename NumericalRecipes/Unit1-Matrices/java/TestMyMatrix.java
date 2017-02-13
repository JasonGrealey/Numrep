//
//  TestMyMatrix.java
//  
//
//  Created by PeterClarke on 25/06/2013.
//  Copyright 2013 __MyCompanyName__. All rights reserved.
//

public final class TestMyMatrix {
	
	public static final void main(String... aArgs){
		log("TestingMyMatix ");
		
		MyMatrix A = new MyMatrix( 3, 5 );
		for( int i=0; i<3;++i ) {
			for(  int j=0; j<5; ++j ) {
				A.setElement(i,j, 10*i+j ) ;
			}
		}

		
		MyMatrix B = new MyMatrix( 3, 5) ;
		for( int i=0; i<3;++i ) {
			for(  int j=0; j<5; ++j ) {
				B.setElement(i,j, 10*i+j+1 ) ;
			}
		}
		
		MyMatrix C ;
		
		C = A.add(B) ;
		
		if ( C == null ) log( "Illegal operation" ) ;
		else {
			log("A");
			A.printIt();
			log("B");
			B.printIt();
			log("C");
			C.printIt();
		}
				
	}
	
	private static void log(String aMessage){
		System.out.println(aMessage);
	}
	
}


