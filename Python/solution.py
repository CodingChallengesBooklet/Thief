import itertools

word = "cowboy"

x = itertools.permutations(word)
for i in x:
    print(i)

a_string = 'cowboy'


def get_permutation(some_string, idx=0):
    if idx == len(some_string) - 1:
        print("".join(some_string))
    for j in range(idx, len(some_string)):
        words_list = [c for c in some_string]
        words_list[idx], words_list[j] = words_list[j], words_list[idx]

        get_permutation(words_list, idx + 1)


permutations = get_permutation(a_string)
print(permutations)
