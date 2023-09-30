
#include<iostream>
using namespace std;
int main(){
    int n;
    int sum=0;
    while(true){
        cout<<"Enter a number = ";
        cin>>n;
        if(n==0){
            break;}

            else if(n<0){
                continue;
                }

        sum+=n;
    }
cout<<"Sum of your all numbers are = "<<sum;
return 0;
}

