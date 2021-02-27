def goes_after(word: str, first: str, second: str) -> bool:
    w = list(word)
    """
        for i in range(len(w)-1):
            if w[i] == first and w[i+1] == second:
                return True
        return False
    """
    f = word.find(first)
    s = word.find(second)

    if f != -1 and s != -1:
        if f + 1 == s:
            return True
    return False



if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'w', 'r') == False
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    assert goes_after('world', 'd', 'w') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
