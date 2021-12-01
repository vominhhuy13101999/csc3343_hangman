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
            TreeNode* leftchild;
            TreeNode* rightchild;
            // std::vector<TreeNode<E>>* children;
            // Comparator* C;
            TreeNode():data(""),leftchild(NULL),rightchild(NULL){
            };
            TreeNode(  string d){
                data=d;
                leftchild = rightchild = NULL;
            } ;
            void addChildren(string d);
    };
class Tree
    {

        public:
            TreeNode* Head;
            int size;

            // std::vector<TreeNode<E>>* children;
            // Comparator* C;
            Tree():Head(NULL){
                
            };
            Tree(string d){
                Head=New TreeNode(d)
            };
            void addChildren(string data);
            TreeNode* search(TreeNode* N,string data);
    };