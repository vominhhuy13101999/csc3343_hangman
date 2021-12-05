#include <bits/stdc++.h>
#include <iostream>
#include <ctime>
#include "search.h"
#include <vector>
#include <functional>
#include <algorithm>

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



int avlTree::get_height(Node* root){
    if (!root){
        return -1;}
    return root->height;
}
Node* avlTree::insert(Node* root,pair<double,int>key){
    // step 1 insert
    if (!root){
        root=new Node(key);}
    else if (key.first < root->data.first)
        root->left=this->insert(root->left,key);
    else    
        root->right=this->insert(root->right,key);

    root->height=1+ max(this->get_height(root->left),this->get_height(root->right));
    int balance=this->get_balance(root);
    

    // step 2 balance
    if (balance>=2){
        int b =this->get_balance(root->left);
        if (b>=1) //left left
            root=this->right_rotate(root);
        else{
            //left right
            root->left=this->left_rotate(root->left);
            root=this->right_rotate(root);
        }
        
    }
    if (balance<=-2){
        int b =this->get_balance(root->right);
        if (b<=-1) //right right
            root=this->left_rotate(root);
        else{
            // right left
            root->right=this->right_rotate(root->right);
            root=this->left_rotate(root);
        }
    }

    return root;
}



int avlTree::get_balance(Node* root){
    if (!root)
        return 0;  
    return this->get_height(root->left)-this->get_height(root->right);
}


Node* avlTree::left_rotate(Node* z){
    Node* y=z->right;
    Node* t2=y->left;
    z->right=t2;
    y->left=z;
    z->height=max(this->get_height(z->left),this->get_height(z->right))+1;
    y->height=max(this->get_height(y->left),this->get_height(y->right))+1;
    return y;

}

Node* avlTree::right_rotate(Node* z){
    Node* y=z->left;
    Node* t2=y->right;
    z->left=t2;
    y->right=z;
    z->height=max(this->get_height(z->left),this->get_height(z->right))+1;
    y->height=max(this->get_height(y->left),this->get_height(y->right))+1;
    return y;
}
Node* avlTree::search(Node* root, int key){
    if(!root){
        if (root->data.first==key)
            return root;
        else if (root->data.first<key)
            return this->search(root->right,key);
        else
            return this->search(root->left,key);
    
    }
    return root;
}


void avlTree::inorder(Node* root){
    if (root){
        inorder(root->left);
        cout<<root->data.first<<endl;
        inorder(root->right);
    }
}

void avlTree::preorder (Node* root){
    if (root){
        cout<<root->data.first<<endl;
        preorder(root->left);
        preorder(root->right);

    }
}


Node* avlTree::get_min(Node* root){
    if (!root->left)
        return root;
    else
        return this->get_min(root->left);
}

