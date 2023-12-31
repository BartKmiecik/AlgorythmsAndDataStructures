def gcd(a, b):
    reminder = a % b
    while reminder != 0:
        a,b = b, reminder
        reminder = a % b
    return b
def lcm(a, b):
    var = gcd(a,b)
    result = (a * b) / var
    return result


# lcm(a, b) = ab/gcd(a,b)
if __name__ == '__main__':
    a, b = map(int, input().split())
    print(int(lcm(a, b)))

