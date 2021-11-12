#include <bits/stdc++.h>
#include <iostream>
#include <ctime>
#include "search.h"
#include <vector>
#include <functional>
using namespace std;
    

    

    

    string* read_dataset(string filename){
        string element;
        int size=370099 ;
        int i=0;
        ifstream myfile (filename);
        string* arr= (string*) malloc(size*sizeof(string));
        if (myfile.is_open())
        {   
            while (i<size-1) {
                    getline(myfile, element);
                    int l=element.length()-1;

                    string e=element.substr(0, l);
                    *(arr+(i)) =e;

                    i++;
                }
            int l=element.length();
            string e=element.substr(0, l);

            *(arr+(i)) =e;  
            cout<<*(arr+(i)) <<endl;
          
            myfile.close();
                }

        
        

        else cout << "Unable to open file";
        return arr;
    }


