n = int(input())
arr = [int(i) for i in input().split(' ')]
dict_arr = {None: []}


for i, val in enumerate(arr):
    new_key = (i, val)
    max_key = None
    for key in dict_arr:
        if key is not None:
            key_val = key[1]
            if key_val < val and len(dict_arr[key]) > len(dict_arr[max_key]):
                max_key = key
        else:
            max_key = key

    dict_arr[new_key] = dict_arr[max_key] + [val]

# print(dict_arr)
max_key = None
for key in dict_arr:
    if len(dict_arr[key]) > len(dict_arr[max_key]):
        max_key = key

answer = dict_arr[max_key]

print(len(answer))
print(' '.join(map(str, answer)))
