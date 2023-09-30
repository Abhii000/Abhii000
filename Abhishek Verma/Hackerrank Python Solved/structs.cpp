#include <iostream>
using namespace std;
struct abhi{
    int age;
    string first_name;
    string last_name;
    int standard;
};

int main(){
    abhi a;
    cin >> a.age >> a.first_name >> a.last_name >> a.standard;

    cout<<a.age<<endl;
    cout<<a.last_name<<", "<<a.first_name<<endl;
    cout<<a.standard<<"\n"<<endl;


    cout << a.age << "," << a.first_name << "," << a.last_name << "," << a.standard;

    return 0;
}