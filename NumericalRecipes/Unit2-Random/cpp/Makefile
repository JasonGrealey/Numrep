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

TestRandom : TestRandom.cpp 
	$(CXX) $(CXXFLAGS) TestRandom.cpp  $(shell gsl-config --cflags) -I $(NUMREPROOT)/MyUtilities/cpp $(shell gsl-config --libs) -o TestRandom
#	$(CXX) $(CXXFLAGS) TestRandom.cpp  $(gsl-config --cflags) -I $(NUMREPROOT)/MyUtilities/cpp -lgsl -o TestRandom

clean   :
	$(RM) $(GARBAGE)

cleanall:
	$(RM) $(GARBAGE)


