from sys import stdin

class stuff:
    def __init__(self, weights:int, values:int):
        self.weights = weights
        self.values = values
        self.value_per_unit = values/weights

def optimal_value(capacity, weights, values):
    value = 0.
    stuff_lst = []
    for i in range(len(weights)):
        stuff_lst.append(stuff(weights[i], values[i]))
    # write your code here
    # print(len(stuff_lst))
    # for n in stuff_lst:
    #     print(n.value_per_unit)
    stuff_lst = sorted(stuff_lst, key=lambda x: x.value_per_unit)
    # for n in stuff_lst:
    #     print(n.value_per_unit)
    # print(capacity > 0)
    while capacity > 0 and len(stuff_lst)>0:
        # print(capacity)
        amount = min(stuff_lst[-1].weights, capacity)
        # print(amount)
        value += amount * stuff_lst[-1].value_per_unit
        stuff_lst.pop(-1)
        capacity -= amount

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    # capacity = 50
    # values = [60, 100, 120]
    # weights = [20, 50, 30]
    opt_value = optimal_value(capacity, weights, values)
    # print(f'Capa: {capacity}, weight: {weights}, values: {values}')
    print("{:.10f}".format(opt_value))
