import time


def fibonacci_partial_sum_naive(from_, to):
    # start = time.time()

    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next % 10, (current + _next) % 10
    # end = time.time()
    # print(end-start)
    return _sum % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))
