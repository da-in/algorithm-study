import sys

N = int(sys.stdin.readline())
num_dict = [(i+1, int(sys.stdin.readline())) for i in range(N)]
num_dict = dict(num_dict)

while True:
    is_delete = False
    temp_dict = dict()

    for k in num_dict.keys():
        if k in num_dict.values():
            temp_dict[k] = num_dict[k]

    if num_dict.keys()==temp_dict.keys():
        break
    else:
        num_dict = temp_dict

print(len(num_dict))
for k in num_dict.keys():
    print(k)