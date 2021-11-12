#include <bits/stdc++.h>
#include <iostream>
#include <ctime>
#include "search.h"
#include <iterator>
#include <algorithm>
#include <time.h>
#include <string>

using namespace std;



int main()
{ 

    string* arr=read_dataset("./4048819.txt");
    int size=370099;
    // for (int i=0; i<size;i++)
    //     cout<<*(arr+i)<<endl;
    string a="tesla";
    int loc=bf_search<string>(arr,size,a);
    cout<<arr[0]<<endl;
    // cout<<arr[loc]<<endl;
    cout<<arr[370098]<<endl;
    return 0;
}