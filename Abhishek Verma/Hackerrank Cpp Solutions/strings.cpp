#include <iostream>
using namespace std;
int main(){
    string a,b;
    cin>>a;
    cin>>b;
    cout<<a.length()<<" "<<b.length()<<endl;
    cout<<a+b<<endl;
    char x=a[0];
    a[0]=b[0];
    b[0]=x;
    cout<<a<<" "<<b;
}