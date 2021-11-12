#ifndef SEARCH_H
#define SEARCH_H
#include <bits/stdc++.h>
#include <functional>

using namespace std;

    string* read_dataset(string filename); //read premake dataset


    template <typename T>
    int bf_search(T arr[], int size,T element);
#endif