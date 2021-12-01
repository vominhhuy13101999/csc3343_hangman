all: SearchTest
SearchTest:
	g++ -std=c++14 main.cpp search.cpp  -o SearchTest.exe