//
//  PracticeJava.java
//  
//
//  Created by PeterClarke on 25/06/2013.
//  Copyright 2013 __MyCompanyName__. All rights reserved.
//


import java.util.Random;
import Jama.*;

//import ptolemy.plot.*;

public final class TestGaussian {
	
	public static final void main(String... aArgs){
		log("Generating 10 Gaussian random numbers ");


        //.......................
        // For all output
        MyFileWriter fw =  new MyFileWriter( ) ;
        
        
        
        //............................................
        //Use my own gaussian random number generator
 
        log("   " );
        log("This is my own Gaussian random number generator" );
 
        MyGaussianPdf gauss = new MyGaussianPdf(0.0,1.0);
        
        int npoints1 = 1000 ;
        Matrix A = new Matrix(npoints1,1);
        
		for (int idx = 0; idx < npoints1; ++idx){
			double x = gauss.next() ;
			log("Generated : " + x);
            A.set(idx,0, x );
			//hist.addPoint(0, x ) ;
		}
        
        fw.writeFile( "myGaussianOutput.txt", A ) ;
        
        //...............................................
        //Use the inbuilt gaussian random number generator
        
        log("   " );
        log("This is the inbuilt Gaussian random number generator" );
        
        Random randomGenerator = new Random();

        int npoints2 = 1000 ;
        Matrix B = new Matrix(npoints2,1);

		for (int idx = 0; idx < npoints2; ++idx){
			double x = randomGenerator.nextGaussian();
			log("Generated : " + x);
            B.set(idx,0, x );
			//hist.addPoint(0, x ) ;
		}
        
        fw.writeFile( "inbuiltGaussianOutput.txt", B ) ;
		
        
        //................................................
		//Test the Numerical integration of my own pdf

        log("   " );
        log("This is the numerical integration of my own Gaussian random number generator" );

		
        double normNumeric = gauss.integralNumeric( -5.0, 5.0 ) ;
        double normNumericII = gauss.integralNumericII( -5.0, 5.0 ) ;  
		double normAnalytic = gauss.integralAnalytic( -5.0, 5.0 ) ;
		log("  Numeric:   NumericII:    Analytic integral " );
        log(""+ normNumeric + "  :   "+ normNumericII + "  :   "+normAnalytic );
		
		
				
	}
	
	private static void log(String aMessage){
		System.out.printf(aMessage+"\n");
	}
	
		
}


