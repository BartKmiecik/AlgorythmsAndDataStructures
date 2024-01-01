def change(money):
    coins = [10, 5, 1]
    min_coins = 0
    for coin in coins:
        res = int(money / coin)
        min_coins += res
        money -= res * coin
    return min_coins


if __name__ == '__main__':
    m = int(input())
    print(change(m))
