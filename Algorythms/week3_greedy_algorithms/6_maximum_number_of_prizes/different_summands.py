def optimal_summands(n):
    summands = []
    if n <= 2:
        summands.append(n)
        return summands
    if n == 3:
        summands.append(1)
        summands.append(2)
        return summands
    next = 1
    total_diff = 1
    summands.append(next)
    while n - total_diff >= next+1 + next+2:
        # print(f'Diff: {n - total_diff} and next: {next}, modulo{modulo}')
        next += 1
        total_diff += next
        summands.append(next)


        # print(f'Diff: {n - total_diff} and next: {next}, modulo{modulo}')
    if n - next != 0:
        summands.append(n-total_diff)

    # write your code here
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
