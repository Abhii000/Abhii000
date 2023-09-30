/*
#include  <iostream>
using namespace std;
int main(){
    int x,y;
    int count=0;
    cin>>x>>y;
    int arr1[x];
    for(int i=0;i<x;i++){
        cin>>arr1[i];
    }
    for(int a:arr1){
        for(int b:arr1){
            if(a<b){
                if((a+b)%y==0){
                count+=1;}
            }
        }
    }
    cout<<count;
    return 0;
}*/

#include <iostream>
using namespace std;

int divisibleSumPairs(int n, int ar[], int k) {
    int count = 0;

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if ((ar[i] + ar[j]) % k == 0) {
                count++;
            }
        }
    }

    return count;
}

int main() {
    int n, k;
    cin >> n >> k;
    int ar[n];

    for (int i = 0; i < n; i++) {
        cin >> ar[i];
    }

    int result = divisibleSumPairs(n, ar, k);

    cout << result << endl;

    return 0;
}
