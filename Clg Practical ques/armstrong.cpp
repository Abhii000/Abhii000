
#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"enter the number";
    cin>>n;
    cout<<"enter the number";
    for(int i=1;i<=n;i++){
        int sum=0;
        int temp=i;
        while(temp!=0){
            int rem=temp%10;
            sum=sum+rem*rem*rem;
            temp=temp/10;}
    
        if(sum==i){
            cout<<i<<endl;

        }
    




}}

