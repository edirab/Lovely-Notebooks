/*
https://riptutorial.com/ru/cplusplus/example/26751/%D0%BC%D1%8C%D1%8E%D1%82%D0%B5%D0%BA%D1%81%D1%8B-%D0%B8-%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D1%8C-%D0%BF%D0%BE%D1%82%D0%BE%D0%BA%D0%BE%D0%B2

Пример починен, еее!
*/
#include <iostream>
#include <thread>
#include <mutex>


using namespace std;

int var = 1;
mutex m;

void add_1(/*int& i, mutex& m*/) { // function to be run in thread
    m.lock();
    var += 1;
    m.unlock();
}

int main() {


    cout << var << endl; // prints 1
    
    thread t1(add_1/*, var, m*/); // create thread with arguments
    thread t2(add_1); // create another thread
    t1.join(); 
	t2.join(); // wait for both threads to finish
    
    cout << var << endl; // prints 3
}