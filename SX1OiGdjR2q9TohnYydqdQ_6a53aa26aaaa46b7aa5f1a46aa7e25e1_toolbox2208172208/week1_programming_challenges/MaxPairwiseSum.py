if __name__ == '__main__':
    _ = input()
    _in = map(int, input().split())
    _in = list(_in)
    _in.sort()
    sum_in = 0
    if len(_in) == 1:
        sum_in = _in[0] * _in[0]
    else:
        sum_in = _in[-1] * _in[-2]
    print(sum_in)