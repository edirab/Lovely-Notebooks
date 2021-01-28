/*
https://ncona.com/2018/08/passing-by-reference-to-a-thread-in-c/

g++ -std=c++0x -pthread  ref_in_thread.cpp
*/


#include <iostream>
#include <thread>

struct container {
  int numThings;
};

void setThings(container& cont)
{
  cont.numThings = 3;
}

int main()
{
  container c;
  std::thread t(setThings, std::ref(c));

  t.join();

  std::cout << c.numThings << "\n\n";
}