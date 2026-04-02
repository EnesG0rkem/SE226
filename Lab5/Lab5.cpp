#include <iostream>
#include <cmath>
using namespace std;

double myOtherFunc(int n){
    if(n > 0) return pow(-1,n+1)/n + myOtherFunc(n-1);
    else return 0;
}

int main(){
    int n;
    cout << "Please enter n:";
    cin >> n;
    cout << myOtherFunc(n) << endl;
}