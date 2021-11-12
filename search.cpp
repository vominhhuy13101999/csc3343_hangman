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
        while (i<size) {
                getline(myfile, element);
                *(arr+(i)) = element;
                i++;
            }
        myfile.close();
            }
    
    

    else cout << "Unable to open file";
    return arr;
}


template <typename T>
    int bf_search(T arr[], int size,T element){
        // equal_to<T> cmp= equal_to<T>{};
        for (int i =0; i<size;i++){
            if (element==arr[i])
                return i;
        }
        return -1;
    }