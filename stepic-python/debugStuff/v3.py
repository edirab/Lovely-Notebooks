with open('dataset.txt') as f:
    # data = f.read().split('\n')
    for line in f.readlines():
        print(line[0], end=' ')
