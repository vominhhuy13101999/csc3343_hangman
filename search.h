#ifndef SEARCH_H
#define SEARCH_H
#include <typeinfo>
#include "Python.h"

#include <bits/stdc++.h>
#include <functional>
#include "bf_search.tpp"    

using namespace std;

    template <typename T>
    int bf_search(T* arr, int size,T element);
    template <typename T>
    int bst_search(T* arr, int low,int high,T element) ;
    // template <typename T>
    // int cs_search(T* arr, int low,int high,T element);
    string* read_dataset(string filename); //read premake dataset


#endif