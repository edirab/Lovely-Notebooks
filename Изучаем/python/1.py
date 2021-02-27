text = '''
When I was One
I had just begun
When I was Two
I was nearly new
'''

words = ['i', 'was', 'three', 'near']


def popular_words(text: str, words: list) -> dict:
    output = dict()
    for i in words:
        output[i] = 0
    # print(output)

    text = text.lower().split()
    print(text)
    for elem in text:
        if elem in words:
            output[elem] += 1
    return output


print(popular_words(text, words))


