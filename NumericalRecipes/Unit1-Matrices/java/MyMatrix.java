//
//  MyMatrix.java
//  
//
//  Created by PeterClarke on 25/06/2013.
//  Copyright 2013 __MyCompanyName__. All rights reserved.
//



public class MyMatrix {
	
	private int rows =0;
	private int columns =0;
	private double[][] data;
	
    //.......................................
	//Constructor
	public MyMatrix( int r, int c )
	{
		rows = r ;
		columns = c ;
		data = new double[rows][columns] ;
		for( int i=0; i<rows;++i ) {
			for(  int j=0; j<columns; ++j )
			{
				data[i][j] = 0.;
			}
		}
	}
		
    //.......................................
	//Add an element
	public void setElement( int i,  int j, double val )
	{
		if( checkIndices( i,j) ) {
			data[i][j] = val ;
		}
	}
	
    //.......................................
	//Add an element
	public double getElement( int i,  int j)
	{
		if( checkIndices( i,j) ) {
			return data[i][j] ;
		}
		else {
			return 0.;
		}
	}
	
    //........................................
    //Always good to add a print method.
	public void printIt() {
		for( int i=0; i<rows;++i ) {
			String line = " ";
			for(  int j=0; j<columns; ++j )
			{
				line += Double.toString(data[i][j]) + " " ;
			}
			System.out.println(line);	
		}
	}
	
	//........................................
	//Add two matrices
	public MyMatrix add( MyMatrix A )
	{

		if( this.rows()==A.rows() &&  this.columns()==A.columns() ) {
			MyMatrix R = new MyMatrix( this.rows(), this.columns() ) ;
			for( int i=0; i<rows;++i ) {
				for(  int j=0; j<columns; ++j )
				{
					R.setElement(i,j, this.getElement(i,j) + A.getElement(i,j) ) ;
				}
			}
			return R ;
		}
		else return null;
	}
				
	//..............................................
	//Multiply two matrices
	public MyMatrix postMultiply( MyMatrix A )
	{
		if( this.columns() == A.rows() ) {
			
			MyMatrix R = new MyMatrix( this.rows(), A.columns() ) ;
			
			for( int i=0; i<this.rows();++i ) {
				for(  int j=0; j<A.columns(); ++j ) {
					double val=0;
					for( int p=0; p< this.columns(); ++p ) { 
						val+= this.getElement( i, p ) * A.getElement( p, j ) ;
					}
				}
			}
			return R ;
		}
		else return null ;
	}
	
	//.................................................
	//Common internal check
	public boolean checkIndices( int i, int j ) 
	{
		if( (i>=0) && (i<rows) && (j>=0) && (j<columns) ) {return true;}
		return false;
	}
			

    //.....................................
	//Basic infomration utilities 
	public int rows() { return rows ; }
	public int columns() { return columns ; }
	
    
    
}


