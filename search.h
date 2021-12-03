#ifndef SEARCH_H
#define SEARCH_H
#include <typeinfo>

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


            TreeNode(  string d){
                data=d;
                left = right = NULL;
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
#endif