
t1 = [['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]


def list_pull(L):
    res = list()

    def unchain(L_):
        print(type(L_), L_)
        if type(L) is not list:
            res.append(L_)
        else:
            for elem in L_:
                unchain(elem)
        return

    for i in L:
        unchain(i)
    return res


r = list_pull(t1)
print(r)