#include <iostream>
#include <cmath>

int main(){
    std::string name;
    int ID;
    std::cout << "What is your name?\n";
    std::cin >> name;
    std::cout << "Hello "<< name<<"\n";


    std::cout << "What is your student ID?\n";
    std::cin >> ID;

    std::cout << "Your ID is "<<ID;


    return 0;
}