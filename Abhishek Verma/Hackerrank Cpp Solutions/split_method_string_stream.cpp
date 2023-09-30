#include <iostream>
#include <sstream>
using namespace std;
int main(){
    string x;
    cin>>x;
    for(int i=0;i<x.length();i++){
        if(x[i]==','){
            cout<<"\n";

        }
        else{cout<<x[i];}
    }

}