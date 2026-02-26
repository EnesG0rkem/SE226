#include <iostream>
#include <cmath>

int main(){

    int p1x;
    int p1y;
    int p2x;
    int p2y;

    std::cout << "Please provide an x coordinate for point 1: ";
    std::cin >> p1x;

    std::cout << "Please provide an y coordinate for point 1: ";
    std::cin >> p1y;

    std::cout << "Please provide an x coordinate for point 2: ";
    std::cin >> p2x;

    std::cout << "Please provide an y coordinate for point 2: ";
    std::cin >> p2y;

    float distance = std::pow((std::pow((p1x+p2x),2) + std::pow((p1y+p2y),2) ),0.5);

    std::cout << "Distance between the points: "<< distance;
    return 0;
}