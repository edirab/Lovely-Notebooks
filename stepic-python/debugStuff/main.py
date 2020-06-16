
t1 = [['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]

r = list()


def pull(L):
    print(type(L), L)
    if type(L) is not list:
        r.append(L)
    else:
        for elem in L:
            pull(elem)
    return


pull(t1)
print(r)