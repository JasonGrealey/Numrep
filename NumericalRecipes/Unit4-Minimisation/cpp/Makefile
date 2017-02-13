# $Id: Makefile,v 1.30 2009/11/11 17:18:14 gcowan Exp $
SHELL = /bin/sh
UNAME = $(shell uname)

################
##linux
CXX          = g++
RM           = rm -f
AR           = ar cru

##Flags
#CXXFLAGS     += -D_DEBUG
CXXFLAGS     = -O3 -gstabs -fPIC -funroll-loops # -Wall

GARBAGE  = $(OBJDIR)/*.o *.so *.rootmap 

SimpleFit : SimpleFit.cpp MyMinimiser.cpp
	$(CXX) $(CXXFLAGS) SimpleFit.cpp MyMinimiser.cpp -o SimpleFit

clean   :
	$(RM) $(GARBAGE)

cleanall:
	$(RM) $(GARBAGE)


