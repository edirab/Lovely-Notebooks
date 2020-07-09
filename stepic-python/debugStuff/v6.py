# https://py.checkio.org/mission/backward-each-word/solve/


def backward_string_by_word(text: str) -> str:
    # your code here
    out = ''

    stack = []
    for i in text:
        if i != ' ':
            stack.append(i)
        else:
            out += ''.join(stack[::-1])
            out += i
            stack = []

    out += ''.join(stack[::-1])
    return out


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")