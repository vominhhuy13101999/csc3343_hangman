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

    // string a="day";

    avlTree* T=new avlTree();
    T->head=NULL;
    int i=0;
    pair<int,int> a(10,1);
    T->head = T->insert(T->head,a );
    ++i;
    pair<int,int> a1(20,1);
    T->head = T->insert(T->head,a1 );
    ++i;
    pair<int,int> a2(30,1);
    T->head = T->insert(T->head,a2 );
    ++i;
    pair<int,int> a3(40,1);
    T->head = T->insert(T->head,a3 );
    ++i;
    pair<int,int> a4(50,1);
    T->head = T->insert(T->head,a4 );
    ++i;
    pair<int,int> a5(25,1);
    T->head = T->insert(T->head,a5 );
    ++i;

    T->preorder(T->head);
    // int loc=bf_search<string>(arr,size,a);
    // int loc1=bst_search<string>(arr,0,size-1,a);
    // int loc2=cs_search<string>(arr,size,a);

    // cout<<arr[0]<<endl;
    // cout<<loc<<endl;
    // cout<<loc1<<endl;
    // cout<<loc2<<endl;


    // cout<<arr[loc]<<endl;
    // cout<<arr[size-1]<<endl;

}