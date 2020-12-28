/*
https://habr.com/ru/company/jugru/blog/469465/

-std=c++98
-std=c++03
-std=c++11
-std=c++14
-std=c++17
-std=c++20

g++ initialization.cpp -std=c++98 -pedantic

Итак, от языка C унаследованы четыре типа инициализации:

- инициализация по умолчанию, (которой, по факту, нет. Это UB)
- копирующая, (знак равенства)
- агрегатная и ( как у массивов через фигурные скобки)
- статическая инициализации. (для статических переменных)

В С++

- прямая инициализация - Круглые скобки Для Всего!
- direct member initializers очень полезны
*/

#include <iostream>
 
using std::cout;

// UB
class Widget {
  public:
    Widget() {}
    int get_i() const noexcept { return i; }
    int get_j() const noexcept { return j; }

  private:
    int i;
    int j;
};


// C++98: member initialiser list
class Widget2 {
  public:
	Widget2() : i(1), j(2) {} 			      // перегружаем конструктор
    Widget2(int i_, int j_) : i(i_), j(j_) {} // member initialiser list
	
    int get_i() const noexcept { return i; }
    int get_j() const noexcept { return j; }

  private:
    int i;
    int j;
};


// C++11: default member initialisers
class Widget3 {
  public:
    Widget3() {}
    int get_i() const noexcept { return i; }
    int get_j() const noexcept { return j; }

  private:
    int i = 5; // default member initialisers
    int j = 6;
};


class Widget4{
	
	public:
		Widget4(int z_){ z = z_; };
		int z;
	
};

int main()
{
	int m = 3;	// copy initialization
	int n(4);	// прямая инициализация. У встроенных типов тоже есть конструкторы
	int k;		// инициализация по умолчанию, UB, позапускать несколько раз
	
    cout << "m " << m << "\n";
	cout << "n " << n << "\n";
	cout << "k " << k << "\n";	
	
	Widget widget;
	cout << "widget " << widget.get_i() << "\n";
	
	//Widget2 widget2(10, 100);
	
	/*
		https://stackoverflow.com/questions/877523/error-request-for-member-in-which-is-of-non-class-type
		Widget2 widget2();
		Не работает потому как комрилятор думает, что Widget2 widget2() - это функция
	*/
	Widget2 widget2;
	cout << "widget2 " << widget2.get_i() << " " << widget2.get_j()  << "\n";
	
	Widget3 widget3;
	cout << "widget3 " << widget3.get_i() << " " << widget3.get_j()  << "\n";
	
	/*
		copy initialization
		не сработает для явного конструктора (explicit)
		
	*/
	Widget4 w4 = -20;
	cout << w4.z << "\n";
	
    return 0;
}