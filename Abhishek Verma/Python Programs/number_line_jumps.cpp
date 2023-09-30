#include <iostream>
using namespace std;
int main(){
    int x1,v1,x2,v2,n;
    int a;
    int arr1[4];
    cin>>x1>>v1>>x2>>v2;
    while(true){
        x1=x1+v1;
        x2=x2+v2;
        if(x1==x2){
            cout<<"YES";
            break;}
        else if(v2>v1){
            cout<<"NO";
            break;}
       else if(x1>x2){
            cout<<"NO";
            break;
       }


}}