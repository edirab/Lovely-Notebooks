import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser()
    # parser.add_argument ('name', nargs='?', default='мир')
    parser.add_argument('-d', '--delay', default=1, type=int, help="Интервал задержки, с")
    parser.add_argument('-r', '--res', default=1, choices=[1, 2], type=int, help="выбор разрешения: 1 - 640 х 480, 2 - 1920 x 1080")
    parser.add_argument('-a', '--annotate', default=1, help="Метка о времени и дате: 1 - True, 0 - False")
    parser.add_argument('-t', '--timeout', default=None)

    return parser


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args()

    print(namespace)
    print("Задержка: {}, {}".format(namespace.delay, type(namespace.delay)))
    print("Тип разрешения: {}, {}".format(namespace.res, type(namespace.res)))