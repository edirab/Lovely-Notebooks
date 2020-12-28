#define N 20

int add(int x, int y); // предварительное объявление функции add() (используется её прототип)

int main()
{
	int m(3);
	int n(4);
	add(m, N);
	
    return 0;
}

int add( int x, int y){
	return x + y;
}