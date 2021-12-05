#ifndef SEARCH_H
#define SEARCH_H
#include <typeinfo>
#include <algorithm>
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


class TreeNode
    {

        public:
            string data;
            TreeNode* left;
            TreeNode* right;
            int value;

            TreeNode(  string d){
                data=d;
                left = right = NULL;
                value=0;
            } ;
    };
class Tree
    {

        public:
            TreeNode* Head;
            int size;

            Tree(){
                Head=NULL;

            };

            TreeNode* addChildren(TreeNode* N,string data);
            TreeNode* search(TreeNode* N,string data);
            void inorder(TreeNode* root);
                
    };


class Node{
    public:
        Node* left;
        Node* right;
        pair<double,int> data; // first is value and second is the index in word lists
        int height;
        Node(pair<double,int> key){
            data=key;
            left=NULL;
            right=NULL;
            height=0;
        }
};



class avlTree{
    public:
        Node* head;

        avlTree(){
            head=NULL;
        };
        int get_height(Node* root);
        Node* insert(Node* root,pair<double,int>key);
        int get_balance(Node* root);
        Node* left_rotate(Node* z);
        Node* right_rotate(Node* z);
        Node* search(Node* root, int a);
        void inorder(Node* root);
        void preorder (Node* root);
        Node* get_min(Node* root);
};
#endif