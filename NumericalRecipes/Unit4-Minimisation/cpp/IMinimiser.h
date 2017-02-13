//
//  IMinimiser.cpp
//  
//
//  Created by Greig Cowan on 18/09/2013.
//  Copyright 2013 __MyCompanyName__. All rights reserved.
//

#include "../../Unit1-Matrices/cpp/MyMatrix.h"

class IMinimiser
{
	public:
		// To set convergence criteria
		virtual void setConvergenceLimit( double conv) = 0;
		virtual void setMaxIterations( int max ) = 0;
		virtual void setStartParameters( MyMatrix params, MyMatrix incs ) = 0;

		// Main minimising method
		virtual MyMatrix minimise( double chisq ) = 0;

		//Methods to report if finished
		virtual bool isFinished() = 0;

		// At the end you will need to know the errors.
		//public Matrix getErrors() 

};
