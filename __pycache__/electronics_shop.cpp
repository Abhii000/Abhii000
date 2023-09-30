/*
#include <iostream>
using namespace std;
int main(){
    int x,y,z;
    int budget;
    cin>>x>>y>>z;
    
    int keyboards[y];
    
    
    for(int i=0;i<y;i++){
        cin>>keyboards[i];
    }

    int drives[z];
    

    for(int j;j<z;j++){
        cin>>drives[j];
    }
    

    budget=keyboards[y-1]+drives[z-1];
    if(budget>x){
        cout<<"-1";
    }
    else{
        cout<<budget;
    }
    return 0;
}*/

#include <iostream>
#include <vector>
using namespace std;

int getMoneySpent(vector<int>& keyboards, vector<int>& drives, int b) {
    int max_cost = -1; // Initialize max_cost to -1 as a flag for not possible to buy

    for (int k : keyboards) {
        for (int d : drives) {
            int cost = k + d;
            if (cost <= b && cost > max_cost) {
                max_cost = cost;
            }
        }
    }

    return max_cost;
}

int main() {
    int b, num_keyboards, num_drives;
    cin >> b >> num_keyboards >> num_drives;

    vector<int> keyboard_prices(num_keyboards);
    vector<int> drive_prices(num_drives);

    for (int i = 0; i < num_keyboards; i++) {
        cin >> keyboard_prices[i];
    }

    for (int i = 0; i < num_drives; i++) {
        cin >> drive_prices[i];
    }

    int result = getMoneySpent(keyboard_prices, drive_prices, b);
    cout << result << endl;

    return 0;
}
