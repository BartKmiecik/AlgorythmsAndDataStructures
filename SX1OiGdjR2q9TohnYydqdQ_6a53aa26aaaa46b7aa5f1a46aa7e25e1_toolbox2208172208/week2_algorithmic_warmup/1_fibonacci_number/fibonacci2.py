def fibonacci_number(n):
    fib_list = [0, 1]
    if n < 2:
        return n
    else:
        for i in range(2, n+1):
            cur = fib_list[i-1]
            prev = fib_list[i-2]
            fib_list.append(cur + prev)
            # print(f'I: {i}, prev: {prev}, cur: {cur}')

    return fib_list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
