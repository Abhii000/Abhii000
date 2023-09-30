#include <iostream>
using namespace std;
int main(){
    int n,val1,val2;
    string a,b,c,d,e,f,g,h,i,j;
    a="one";
    b="two";
    c="three";
    d="four";
    e="five";
    f="six";
    g="seven";
    h="eight";
    i="nine";
    cin>>val1;
    cin>>val2;
    for(int k=val1;k<=val2;k++){
        if(k<=9){
            if(k==1){
                cout<<a<<endl;}
            else if(k==2){
                cout<<b<<endl;}
            else if(k==3){
                cout<<c<<endl;}
            else if(k==4){
                cout<<d<<endl;}
            else if(k==5){
                cout<<e<<endl;}
            else if(k==6){
                cout<<f<<endl;}
            else if(k==7){
                cout<<g<<endl;}
                else if(k==8){
                    cout<<h<<endl;}
                else if(k==9){
                    cout<<i<<endl;}}
        else{if(k%2==0){cout<<"even"<<endl;}
            else{cout<<"odd"<<endl;}}
            
        
            
        



    }

}
