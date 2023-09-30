#include<iostream>
using namespace std;
int main(){
    int a,b,c,d,e;
    
    cin>>a;
    for(int i=0;i<a;i++){
        int arr1[3];
        for(int j=0;j<3;j++){
            cin>>arr1[j];}

        if(abs(arr1[2]-arr1[0])<abs(arr1[2]-arr1[1])){
            cout<<"Cat A"<<endl;}

        else if(abs(arr1[2]-arr1[0])==abs(arr1[2]-arr1[1])){
            cout<<"Mouse C"<<endl;
        }
        else{cout<<"Cat B"<<endl;}
    }
    return 0;
}