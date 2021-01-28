/*
https://nrecursions.blogspot.com/2014/08/mutex-tutorial-and-example.html

Compile and run it using  

g++ -std=c++0x -pthread mutex2.cpp

./thread 
*/

#include <iostream>
#include <thread>
#include <mutex>


std::mutex m;//you can use std::lock_guard if you want to be exception safe 
int i = 0; 
void makeACallFromPhoneBooth() 
{

    //The other men wait outside 
    m.lock();// one man gets a hold of the phone booth door and locks it. 
      //man happily talks to his wife from now....
      std::cout << i << " Hello Wife" << std::endl;
      i++;//no other thread can access variable i until m.unlock() is called
      //...until now, with no interruption from other men
    m.unlock();//man unlocks the phone booth door 
}

int main() 
{
    //This is the main crowd of people uninterested in making a phone call

    //man1 leaves the crowd to go to the phone booth
    std::thread man1(makeACallFromPhoneBooth);
    //Although man2 appears to start second, there's a good chance he might
    //reach the phone booth before man1
    std::thread man2(makeACallFromPhoneBooth);
    //And hey, man3 also joined the race to the booth
    std::thread man3(makeACallFromPhoneBooth);

    man1.join();//man1 finished his phone call and joins the crowd
    man2.join();//man2 finished his phone call and joins the crowd
    man3.join();//man3 finished his phone call and joins the crowd
    return 0;
}