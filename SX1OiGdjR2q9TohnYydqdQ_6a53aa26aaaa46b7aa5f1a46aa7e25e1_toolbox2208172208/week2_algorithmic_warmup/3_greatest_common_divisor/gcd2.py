import time


def gcd(a, b):
    start = time.time()
    reminder = a % b
    while reminder != 0:
        # print(f'Reminder of: {a}, {b} is {reminder}')
        a,b = b, reminder
        reminder = a % b

    end = time.time()
    print(end - start)
    # print(b)
    return b


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
