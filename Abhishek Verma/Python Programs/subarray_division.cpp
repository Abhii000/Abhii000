/*
#include <iostream>
using namespace std;
int main(){
    int a,b,c,x,y;

    cin>>a;
    int arr1[a];
    for(int i=0;i<a;i++){
        cin>>arr1[i];
    }
    cin>>b>>c;
    int k=0;
    for(int l:arr1){
        for(int t:arr1){
        
            if(l+t==b){
                k+=1;
                break;}}
                }
    cout<<k;
    return 0;

}*/

#include <iostream>
#include <vector>

using namespace std;

int birthday(vector<int> s, int d, int m) {
    int ways = 0;

    for (int i = 0; i <= s.size() - m; i++) {
        int sum = 0;
        for (int j = 0; j < m; j++) {
            sum += s[i + j];
        }
        if (sum == d) {
            ways++;
        }
    }

    return ways;
}

int main() {
    int n;
    cin >> n;
    vector<int> s(n);

    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }

    int d, m;
    cin >> d >> m;

    int result = birthday(s, d, m);

    cout << result << endl;

    return 0;
}
