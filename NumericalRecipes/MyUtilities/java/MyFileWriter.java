//
//  MyFileWriter.java
//  
//  A minimal I/O package to write data to a text file.
//  It is accepted in the form of a matrix.
//  It writes the Matrix literally to a file.
//  For use in Numerical Recipes course.
//
//  Created by PeterClarke on 30/07/2013.
//

import java.util.*;
import java.io.*;
import Jama.*;


public class MyFileWriter {
		
	//.......................
	// Constructor
	public MyFileWriter ( ) { }
	
	//.......................
	//Writes a Matrix to a file
	public boolean writeFile( String filename, Matrix payload ) {
	
		int nrows=payload.getRowDimension();
		int ncols=payload.getColumnDimension();

		FileWriter fw = null ;
		PrintWriter pw = null;
		
		boolean luck=false;
		
		try {
			//File file = new File("testout.txt");
			fw = new FileWriter(filename);
			pw = new PrintWriter(fw);
			
			for( int irow=0; irow<nrows; ++irow ) {
				String line = "" ;
				for( int icol=0; icol< ncols; ++icol ) {
					double val = payload.get(irow,icol);
					line += Double.toString( val )+"  " ;
				}
				
				pw.println(line);
			}
			luck = true ;
		} 
		catch (IOException e) {
			e.printStackTrace();
			luck = false;
		} 
		finally {
			if (pw != null) pw.close();
		}	
		
		return luck ;
	}

}


