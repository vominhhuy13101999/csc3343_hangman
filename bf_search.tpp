
using namespace std;

template <typename T>
int bst_search(T* arr, int low,int high,T element){
    int mid;
    if (high>=low){
        mid=(high+low)/2;
        if (arr[mid]==element)
            return mid;
        else if (arr[mid]>element)
            return bst_search(arr,low,mid-1,element);
        else
            return bst_search(arr,mid+1,high,element);
    }
    else
        return high;
    
}
template <typename T>
int bf_search(T* arr, int size,T element){

        for (int i =0; i<size;i++){
            if((*(arr+i))==(element))
                return i;
            

}
        
        return -1;
    }
template <typename T>
int cs_search(T* arr, int size,T element){
    int low=0;
    int high=size-1;
    do {
        if (arr[low]==element)
            return low;
        else
            low++;}
    while (high>=low);
    
    return -1;
    
}