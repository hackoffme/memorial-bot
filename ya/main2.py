from unittest import result


def hamming2(x_str, y):
    x = int(x_str, 2)
    count, z = 0, x ^ y
    while z:
        count += 1
        z &= z - 1 
    return count


if __name__ == '__main__':
    res = []
    # len_x, count = map(int, input().split())
    # binar = []
    # for _ in range(count):
    #     i, v = input().split()
    #     binar.append((i, v))
    len_x = 5
    count = 3
    binar = [('01000', '00110'), ('00000', '11111'), ('00001', '00111')]
    m = []
    for item in binar:
        m=[]
        for i in range(2**len_x):
            x = hamming2(item[0], i)
            y = hamming2(item[1], i)
            m.append([i, x, y, x+y])

        m = sorted(m, key = lambda x: x[2])
        result = m[0][0]
        result = str(bin(result))[2::]
        res.append(f'{"0"*(len_x-len(result))}{result}')

    print(*res, sep='\n')
# 