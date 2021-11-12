all: SearchTest
SearchTest:
	g++ -std=c++14 search.cpp main.cpp -o SearchTest.exe