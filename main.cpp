#include <bits/stdc++.h>
#include <iostream>
#include <ctime>
#include "search.h"
#include <iterator>
#include <algorithm>
#include <time.h>
#include <string>

using namespace std;
template <typename T>
int cs_search(T* arr, int low,int high,T element){
    if (arr[low]==element)
        return low;
    else if (low==high)
        return -1;
    else
        return cs_search(arr,low+1,high,element);
    
}

int main()
{ 

    string* arr=read_dataset("./4048819.txt");
    int size=370099;
    // for (int i =319690; i<319700;i++)
    //     cout<<*(arr+i)<<endl;
    string a="tesla";
    int loc=bf_search<string>(arr,size,a);
    int loc1=bst_search<string>(arr,0,size-1,a);
    int loc2=bst_search<string>(arr,0,size-1,a);

    cout<<arr[0]<<endl;
    cout<<loc<<endl;
    cout<<loc1<<endl;
    cout<<loc2<<endl;


    cout<<arr[loc]<<endl;
    cout<<arr[size-1]<<endl;

    return 0;
}