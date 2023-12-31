import time


def fibonacci_number(n):
    start = time.time()
    fib_list = [0, 1]
    if n < 2:
        return n
    else:
        prev = 0
        cur = 1
        for i in range(2, n+1):
            prev, cur = cur % 10, (prev + cur) % 10

    end = time.time()
    # print(end-start)
    return cur


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_number(n))
