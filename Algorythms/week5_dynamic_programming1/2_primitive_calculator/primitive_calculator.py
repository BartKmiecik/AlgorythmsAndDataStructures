m = {0: 0, 1: 0, 2: 1, 3: 1}
result = []
def forward_pass(n):
    # operations add 1, multiply by 2, multiply by 3
    if n < 4:
        return
    for i in range(4, n+1):
        mod3 = i % 3
        if mod3 != 0:
            m3 = i - mod3
            m3 = m[m3]
        else:
            m3 = i // 3
            m3 = m[m3] + 1
        m3min = m3 + mod3

        mod2 = i % 2
        if mod2 != 0:
            m2 = i - mod2
            m2 = m[m2]
        else:
            m2 = i // 2
            m2 = m[m2] + 1
        m2min = m2 + mod2

        m[i] = min(m3min, m2min)


def backward_pass(n):
    result.append(n)
    if n > 2:
        values = {}
        values[n-1] = m[n-1]
        values[n//2] = m[n//2] + n % 2
        values[n//3] = m[n//3] + n % 3
        # print(values)
        values = dict(sorted(values.items(), key=lambda item: item[1]))
        # print(values)
        key = list(values.items())[0]
        # print(values)
        # print(key[0])
        backward_pass(key[0])


def compute_operations(n) -> list:
    forward_pass(n)
    backward_pass(n)
    result.reverse()
    return result

if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
