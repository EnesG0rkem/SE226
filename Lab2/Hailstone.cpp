#include <iostream>
int main(){
    int x;
    int step = 0;
    std::cout << "Please give a number: ";
    std::cin >> x;

    std::cout << x;
    while(x != 1){
        step++;
        if(x % 2 == 0) x/=2;
        else x = x*3 + 1;
        std::cout << " -> " << x;
    }

    std::cout << "\nTotal number of steps: " << step << std::endl;

}