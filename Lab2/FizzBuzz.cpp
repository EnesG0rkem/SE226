#include <iostream>
int main(){
    int x;
    int fizzCounter = 0;
    int buzzCounter = 0;
    int fizzBuzzCounter = 0;

    while (true)
    {
        std::cout << "Please give an integer in the range of 10 and 100: ";
        std::cin >> x;
        if(x<10 || x>100) continue;
        else break;

    }

    for(int num=1; num < x+1; num++){
        if(num % 7 == 0) continue;
        if(num % 3 == 0 && num % 5 == 0){
            std::cout << "FizzBuzz" << std::endl;
            fizzBuzzCounter++;
        }
        else if(num % 3 == 0 ){
            std::cout << "Fizz" << std::endl;
            fizzCounter++;
        }
        else if(num % 5 == 0){
            std::cout << "Buzz" << std::endl;
            buzzCounter++;
        }
        else std::cout << num << std::endl;
    }
    
    std::cout << "--- Summary ---" <<
                "\nFizz count: " << fizzCounter <<
                "\nBuzz count: " << buzzCounter <<
                "\nFizzBuzz count: " << fizzBuzzCounter << std::endl;
    return 0;
}