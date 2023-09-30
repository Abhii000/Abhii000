#include <iostream>
using namespace std;
int main(){
    int x,y;
    cin>>x>>y;
    int arr1[x];
    for(int i=0;i<x;i++){
        cin>>arr1[i];
    }
    int z,l,j;
    j=0;
    cin>>z;
    for(int l:arr1){
        j=j+l;

    }
    int f,g;
    f=(j-arr1[y])/2;
    g=z-f;
    if(g==7){
        cout<<"Bon Appetit";
    }
    else if(g==0){
        cout<<"Bon Appetit";
    }
    else{cout<<g;}
    return 0;
}