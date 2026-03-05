#include <iostream>
#include <string>
using namespace std;
int main(){
    int x;
    while (true)
    {
        std::cout << "Please give an integer in the range of 3 and 9: ";
        std::cin >> x;
        if(x<3 || x>9) continue;
        else break;
    }
    for(int i = 1; i < x+1 ; i++){
        std::cout << std::string(i,'*') << std::endl;
    }
    for(int i = x+1; i > 0 ; i--){
        std::cout << std::string(i,'*') << std::endl;
    }
}