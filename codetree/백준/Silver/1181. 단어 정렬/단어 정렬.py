import sys

def sort_fun(arr):
    arr = list(set(arr))
    sorted_arr = sorted(arr, key=lambda x: (len(x), x))
    return sorted_arr

n = int(sys.stdin.readline())
word = []
for i in range(n):
    word.append(sys.stdin.readline().rstrip())

sorted_word = sort_fun(word)
for i in sorted_word:
    print(i)