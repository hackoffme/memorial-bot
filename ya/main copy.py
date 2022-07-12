
if __name__ == '__main__':
    m = '[[[[[[1]]]], []]]'
    m = '[1, 2, 3, 5, [5, 5], 12, [10, [6, 6, 6]]]'
    m = list(map(int, m.translate({ord(i): None for i in '[],'}).split()))
    d = {i: m.count(i) for i in set(m)}
    l = dict(filter(lambda x: x[1] == max(d.values()), d.items(), ))
    print(*l.keys(), sep=' ')

