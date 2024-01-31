from sys import stdin


def decode(words: str):
    word_lines = words.splitlines()
    cont_dict = {}
    for line in word_lines:
        # print(line)
        number, word = line.split(' ')
        # print(number)
        # print(word)
        cont_dict[int(number)] = word
    answer = ''
    counter = 2
    i = 1
    while i < len(word_lines)+1:
        print(f'I:{i}, {cont_dict[i]}')
        answer += f'{cont_dict[i]} '
        i += counter
        counter += 1

    print(answer)
    return answer


# input_values = stdin.read()
# assert input_values

# decode(input_values)

s1 = {1,2}
s2 = {2,3}

print(s1&s2)