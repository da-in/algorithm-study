import sys

text = sys.stdin.readline().rstrip()

count = text.count('a')

result = sys.maxsize

for start in range(len(text)):
    b = 0
    for i in range(count):
        j = (start + i) % len(text)
        if text[j] == 'b':
            b += 1
    result = min(result, b)

print(result)
