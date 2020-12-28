#include <iostream>
 
int add(int x, int y); // предварительное объявление функции add() (используется её прототип)


/*
Объявить можно сколько угодно раз, определить - только один
*/
int f();
int f();
int f();
int f();
int f();

int f(){
	return 42;
}


int main()
{
	int m(3);
	int n(4);
	
    std::cout << "The sum of 'm' and 'n' is: " << add(m, n) << std::endl;
    return 0;
}

int add( int x, int y){
	return x + y;
}