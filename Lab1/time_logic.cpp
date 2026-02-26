#include <iostream>
#include <cmath>

int main(){

    int seconds;
    std::cout << "Please type the seconds you want to convert\n";
    std::cin >> seconds;
    int copy = seconds;

    int hours = seconds / 3600;
    seconds -= hours*3600;
    int minutes = seconds/ 60;
    seconds -= minutes*60;

    std::cout << copy<< " seconds is "<< hours<< " hours, "<< minutes<< " minutes and "<< seconds << " seconds";

    return 0;
}