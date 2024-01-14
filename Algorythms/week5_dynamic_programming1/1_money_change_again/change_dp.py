def change(money):
    # denomination: 1 3 4
    if money > 3:
        money = (money // 4) + 1

    return int(money)


if __name__ == '__main__':
    m = int(input())
    print(change(m))
