#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, q; // n: number of variable-length arrays, q: number of queries
    cin >> n >> q;
    
    // Create a vector of vectors to represent the variable-length arrays
    vector<vector<int>> variableArrays;

    // Read the variable-length arrays and store them in variableArrays
    for (int i = 0; i < n; i++) {
        int k; // size of the current array
        cin >> k;
        vector<int> arr(k); // create a vector of size k for the current array
        for (int j = 0; j < k; j++) {
            cin >> arr[j];
        }
        variableArrays.push_back(arr);
    }

    // Process the queries
    for (int i = 0; i < q; i++) {
        int x, y; // x: index of the array, y: index within the array
        cin >> x >> y;
        cout << variableArrays[x][y] << endl;
    }

    return 0;
}

/*#include <iostream>
#include <string>
using namespace std;

int main() {
    int a, b;
    cin >>a>>b;
    int arr2[9][9];
    string array;
    cin.ignore();
    // Read array values
    for (int i=0;i<a;i++) {
        
        getline(cin,array);
        int n=0;
        for (int k=2;k<array.length();k=k+2) {
            arr2[i][n]=array[k]-'0';
            n+= 1;
        }
    }

    // Read and output values from arr2
    int c, d;
    for (int j=0;j<b;j++){
        cin>>c>>d;
        cout<<arr2[c][d]<<endl;
    }
    return 0;
}
*/