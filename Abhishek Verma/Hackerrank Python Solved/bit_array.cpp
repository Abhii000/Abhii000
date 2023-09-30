#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

unsigned long long mask[40000000];

unsigned insert(unsigned x) {
    unsigned res = (mask[x >> 6] & (1ULL << (x & 0x3F))) == 0;
    mask[x >> 6] |= 1ULL << (x & 0x3F);
    return res;
}

int main() {
    unsigned N, S, P, Q;
    cin >> N >> S >> P >> Q;
    unsigned x = S;
    unsigned ans = 0;
    ans += insert(x);
    for (unsigned i = 1; i < N; i++) {
        x = (1LL * x * P + Q) % 2147483648;
        ans += insert(x);
    }
    cout << ans << endl;
    return 0;
}

/*
#include <iostream>
using namespace std;
int main(){
    int N,S,P,Q;
    cin>>N>>S>>P>>Q;
    int a[N];
    a[0] = S;
for (int i = 1;i<=N-1;i++){
    a[i] = a[i-1]*P+Q;
    }
    int reader=0;
    int dist=0;
    for(int k:a){
        //cout<<k<<" ";
        if(k!=dist){
            dist=k;
            reader++;
        }
    }
    cout<<reader;
}*/
