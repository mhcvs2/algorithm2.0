

def t1(target, data):
    mi = 0
    ma = len(data)-1
    while mi < ma:
        mid = int((mi + ma) / 2)
        if data[mid] == target:
            return mid
        if data[mid] > target:
            ma = mid - 1
        else:
            mi = mid + 1
    return None


def t2(target, data):
    mi = 0
    ma = len(data)-1
    while mi < ma:
        mid = int((mi + ma) / 2)
        if data[mid] == target:
            while mid >= 0:
                if data[mid] != target:
                    break
                mid -= 1
            return mid + 1
        if data[mid] > target:
            ma = mid - 1
        else:
            mi = mid + 1
    return None


if __name__ == '__main__':
    print(t2(4, [4,4,4,4, 4,5,6,7]))

