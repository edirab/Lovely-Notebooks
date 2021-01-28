/*
https://codengineering.ru/post/23666
*/

#include <iostream>
#include <thread>

int main() {
  std::cout << "The number of concurrent threads is " << std::thread::hardware_concurrency() << "\n";
}