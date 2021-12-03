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
                    
                    int l=element.length();
                    // cout<<l<<endl;
                    string e=element.substr(0, l);
                    *(arr+(i)) =e;

                    i++;
                }
            int l=element.length();
            string e=element.substr(0, l);

            *(arr+(i)) =e;  
            // cout<<*(arr+(i)) <<endl;
          
            myfile.close();
                }

        
        

        else cout << "Unable to open file";
        return arr;
    }




TreeNode* Tree::addChildren(TreeNode* N,string data){
    
    if (!N){
        N=new TreeNode(data);
        return N;


    }
    if (data < N->data)
        N->left = this->addChildren(N->left, data);
    else
        N->right = this->addChildren(N->right, data);
 
    return N;
}
TreeNode* Tree::search(TreeNode* N,string d){
    if (!N || N->data==d){
        // cout<<N->data<<endl;
        return N;
    }
    else if(N->data>d){
        // cout<<N->data<<endl;

        return search(N->left,d);
    }
    else{
        // cout<<N->data<<endl;

        return search(N->right,d);}

}
void Tree::inorder(TreeNode* root)
{
    if (root != NULL) {
        inorder(root->left);
        cout<<root->data<<endl;
        inorder(root->right);
    }
}