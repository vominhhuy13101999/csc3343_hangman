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

    // string* arr=read_dataset("./4048819.txt");

    string* arr=read_dataset("./text.txt");
    int size=370099;

    string a="day";

    Tree* T=new Tree();
    

    // int loc=bf_search<string>(arr,size,a);
    // int loc1=bst_search<string>(arr,0,size-1,a);
    // int loc2=cs_search<string>(arr,size,a);

    // cout<<arr[0]<<endl;
    // cout<<loc<<endl;
    // cout<<loc1<<endl;
    // cout<<loc2<<endl;


    // cout<<arr[loc]<<endl;
    // cout<<arr[size-1]<<endl;
    for ( int i=74822; i<size;i++){
        cout<<arr[i]<<endl;
        cout<<i<<endl;
        T->Head=T->addChildren(T->Head,arr[i]);
    }
    cout<<"reach here"<<endl;

    TreeNode *Head=T->search(T->Head,a);
    if (!Head)
        cout<<"not found"<<endl;
    else
        cout<<Head->data<<endl;
    return 0;
}