def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10
        _sum += current % 10

    return _sum % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
