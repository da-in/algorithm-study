from itertools import combinations

def solution(word):
    answer = 0
    string = ""
    dictionary = []
    string = "AEIOU" * 5
    for i in range(1, 6):
        dictionary += list(map(lambda x: "".join(x), combinations(string, i)))
    dictionary = list(set(dictionary))
    dictionary.sort()
    return dictionary.index(word) + 1
