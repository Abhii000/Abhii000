#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[n][5];

    for (int a = 0; a < n; a++) {
        for (int i = 0; i < 5; i++) {
            cin >> arr[a][i];
        }
    }

    int firstStudentSum = 0;
    for (int j = 0; j < 5; j++) {
        firstStudentSum += arr[0][j]; // Calculate the sum of marks for the first student
    }

    int check = 0;
    for (int b = 1; b < n; b++) { // Start from the second student
        int sum = 0;
        for (int j = 0; j < 5; j++) {
            sum += arr[b][j];
        }
        if (sum > firstStudentSum) {
            check++;
        }
    }

    cout << check << endl;
    return 0;
}
