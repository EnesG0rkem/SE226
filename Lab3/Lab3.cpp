#include <iostream>

using namespace std;

void swapValues(int* p1, int* p2){
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void printArray(int* arr, int size){
    for(int i = 0; i < size ; i ++){
        cout << *(arr + i) << " ";
    }
    cout << endl;
}

int findSum(int* arr, int size){
    int sum = 0;
    for(int i = 0; i < size ; i ++){
        sum += *(arr + i);
    }

    return sum;
}

void shiftRight(int* arr, int size){
    int last = *(arr+size-1);
    int prev = *(arr);
    int curr = 0;

    for(int i = 1; i < size ; i ++){
        curr = *(arr + i);
        *(arr + i) = prev;
        prev = curr;

    }
    *arr = last;
}

int* createArray(int size){
    int* arr;
    arr = new int[size];
    return arr;
}

void deleteArray(int* arr){
    delete[] arr;
}

int main(){
    int size = 0;

    cout << "Please give array size: ";
    cin >> size;
    int* arr = createArray(size);
    cout << "Please enter values: " << endl;
    for ( int  i = 0 ; i < size ; i ++){
        cin >> *(arr + i);
    }

    printArray(arr, size);

    cout << "Sum of elements: " << findSum(arr, size) << endl; 

    cout << "----------------------------------"<< endl;

    int* pA;
    cout << "Enter first number: ";
    int a = 0;
    cin >> a;
    pA = &a;



    int* pB;
    cout << "Enter second number: ";
    int b;
    cin >> b;
    pB = &b;


    cout << "Swapping two numbers"<< endl;

    cout << "Before swap" << endl <<
    "a = " << *pA << endl <<
    "b = " << *pB << endl;

    swapValues(pA, pB);

    cout << "After swap" << endl <<
    "a = " << *pA << endl <<
    "b = " << *pB << endl;

    cout << "----------------------------------"<< endl;

    cout << "Shiting array to the right..."<< endl;

    shiftRight(arr, size);

    cout << "Array after right shift:" << endl;

    printArray(arr, size);

    cout << "Deleting array..."<< endl;
    deleteArray(arr);
    cout << "Memory relased successfully"<< endl;

    return 0;
}

