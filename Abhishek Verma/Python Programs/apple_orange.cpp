#include <iostream>
#include <string>
using namespace std;
int main(){
    int s,t,a,b,m,n;
    string apples,oranges;
    int apple_count=0;
    int orange_count=0;    
    
    cin>>s>>t;
    int home[t-s];
    n=0;
    for(int z=s;z<=t;z++){
        home[n]=z;}
        n+=1;
    cin>>a>>b;
    cin>>m>>n;
    int arr1[m];
    int arr2[n];
    for(int k=0;k<m;k++){
        cin>>arr1[k];
    }
    for(int l=0;l<n;l++){
        cin>>arr2[l];
    }
    for(int y:arr1){
    
        if (y+a>=s && y+a<=t){
            apple_count+=1; } }
    for(int x:arr2){
        if(x+b>=s && x+b<=t){
            orange_count+=1;
        }
    }
    cout<<apple_count<<endl;
    cout<<orange_count<<endl;
    return 0;
}