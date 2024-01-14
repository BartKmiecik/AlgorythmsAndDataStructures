def change(money):
    # denomination: 1 3 4
    if money == 0:
        return 0
    if money == 2:
        return 2
    if money <= 4:
        return 1
    if money > 4:
        mod4 = money % 4
        money = money // 4
        if mod4 > 0:
            money += 1

    return int(money)


if __name__ == '__main__':
    m = int(input())
    print(change(m))
