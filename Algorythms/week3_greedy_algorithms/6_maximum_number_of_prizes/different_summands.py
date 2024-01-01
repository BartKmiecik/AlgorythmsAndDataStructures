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
    modulo = next + next+1
    total_diff = next
    while n - total_diff >= modulo:
        # print(f'Diff: {n - total_diff} and next: {next}, modulo{modulo}')
        summands.append(next)
        next += 1
        total_diff += next
        # print(f'Diff: {n - total_diff} and next: {next}, modulo{modulo}')
    if n - next != 0:
        summands.append(n-next)

    # write your code here
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
