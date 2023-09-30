#include <iostream>

using namespace std;
int main(){
    int arr1[4];
    int x=0;
    for(int a=0;a<4;a++){
        cin>>arr1[a];
        if(arr1[a]>x){
            x=arr1[a];
        }
    }

    cout<<x;
}