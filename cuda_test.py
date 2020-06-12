from numba import jit, cuda
import numpy as np

# измерить время выполнения
from timeit import default_timer as timer   

# нормальная функция для запуска на процессоре

def func(a):                                
    for i in range(10000000):
        a[i]+= 1      

# функция оптимизирована для работы на GPU

@jit(target ="cuda")                         
def func2(a):
    for i in range(10000000):
        a[i]+= 1


n = 10000000                            
a = np.ones(n, dtype = np.float64)
b = np.ones(n, dtype = np.float32)

start = timer()
func(a)
print("without GPU:", timer()-start)    

start = timer()
func2(a)
print("with GPU:", timer()-start) 