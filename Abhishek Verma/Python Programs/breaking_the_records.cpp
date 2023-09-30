#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[n];

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int low = 0, high = 0;
    int low_check = arr[0], high_check = arr[0];

    for (int i = 1; i < n; i++) {
        if (arr[i] > high_check) {
            high++;
            high_check = arr[i];
        } else if (arr[i] < low_check) {
            low++;
            low_check = arr[i];
        }
    }

    cout << high << " " << low << endl;

    return 0;
}
