#include <iostream>

class MyClass;

//Исользуем только чать из стандартного пространства имён
using std::cout;

// Создали своё пространство имён
namespace MyName {
	
	void f1();
	void f2();
	
	// Класс задаёт своё пространство имён
	class MyClass {
	
	public:
		void hello(){
			cout << "Hello! \n";
		}
	};
}

namespace Alias = MyName;
//using namespace Alias;


void MyName::f1(){
	cout << "f1 \n";
}

void MyName::f2(){
	cout << "f2 \n";
}



int main(int argc, char* argv[]){
	
	MyName::MyClass A;
	A.hello();
	
	MyName::f1();
	MyName::f2();
	
	
	
	Alias::MyClass B;
	B.hello();
	
}