import json
from unicodedata import name
from unittest import result


def linear(list):
    flag = True
    while(flag):
        flag = False
        new_list = []
        for item in list:
            if type(item) == type([]):
                flag = True
                new_list.extend(item)
            else:
                new_list.append(item)
        # print(list)
        list = new_list
    return list


def counter(list):
    counter_list = {}
    for item in list:
        if counter_list.get(item):
            counter_list[item] += 1
        else:
            counter_list[item] = 1

    return sorted(counter_list.items(), key=lambda x: x[1], reverse=True)


def main(m):
    list_var = list(counter(linear(m)))
    result = []
    max = list_var[0][1]
    for key, value in list_var:
        if value == max:
            result.append(key)
    return result


if __name__ == '__main__':

    m = input()
    # m = '[[[[[[1]]]], []]]'
    m = json.loads(m)
    if len(m) == 1:
        while(True):
            if type(m) == type([]):
                m = m[0]
            else:
                result = [m]
                break
    else:
        result = main(m)
    
    print(*sorted(result), sep=' ')
