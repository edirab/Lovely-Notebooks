#!/usr/bin/python3

"""
Case 1
Импорт пакета без __init__ файла:
"""
#from pkg1.module_1 import hello, Pi
#from pkg1.module_2 import bark

"""
Case 2
Так сделать не получится без файла инициализации.
Ничего из ниже не сработает
"""
#import pkg1.module_1.hello
#from pkg1 import *

"""
Case 3
Теперь мы создали файл инит и в нём импортировали всё через *.
Не очень хорошая практика, зато быстро и удобно.
Теперь можно импортировать из пакета непосредственно ф-ии, классы, константы и т.д. 
без указания имени модуля
"""
from pkg1 import hello, bark, Pi


def main():
    print("Я разобрался с модулями и пакетами в Python!", Pi)
    hello()
    bark()


if __name__=="__main__":
    main()
