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

MyFileReader : TestMyFileReader.cpp
	$(CXX) $(CXXFLAGS) TestMyFileReader.cpp MyFileReader.cpp $(NUMREPROOT)/Unit1-Matrices/cpp/MyMatrix.cpp -o TestMyFileReader

clean   :
	$(RM) $(GARBAGE)

cleanall:
	$(RM) $(GARBAGE)


