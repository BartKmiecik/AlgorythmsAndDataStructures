from itertools import permutations

def card_value(card, maxi):
    values = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, }
    result = 0
    for i in reversed(range(maxi+1)):
        if i < len(card):
            result += int(card[i]) * 10 ^ i
        else:
            result += int(card[0]) * 10 ^ i

    # print(f'Card: {card}, value: {result}')
    return result

def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest



def largest_num(number):
    maxi = max(number)
    # print(maxi)
    sor = sorted(number, key=lambda x: card_value(x, len(maxi)), reverse=True)
    # print(sor)
    # number.sort(reverse=True,key= lambda x : (x[1] if len(x) > 1 else x[0]))
    # print(number)
    result = ''
    # print(sor)
    for n in sor:
        result += n
    # print(number)
    # print(result)
    return result

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_num(input_numbers))
