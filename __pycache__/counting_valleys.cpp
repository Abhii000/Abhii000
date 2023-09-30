#include <iostream>
using namespace std;

int main() {
    int x;
    string hill;
    cin >> x;
    cin >> hill;
    int uphills_cover = 0;
    int level = 0;  // Initialize altitude level

    for (char a : hill) {
        if (a == 'U') {
            level++;
            if (level == 0) {
                uphills_cover++;
            }
        } else if (a == 'D') {
            level--;
        }
    }

    cout << uphills_cover << endl;
    return 0;
}
