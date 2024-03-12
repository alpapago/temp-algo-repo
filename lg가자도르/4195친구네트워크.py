def find(x):
    if friend[x] != x:
        friend[x] = find(friend[x])
    return friend[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        friend[a] = b
        number[b] += number[a]


for _ in range(int(input())):
    friend = dict()
    number = dict()
    for _ in range(int(input())):
        a, b = input().split()
        if a not in friend:
            friend[a] = a
            number[a] = 1
        if b not in friend:
            friend[b] = b
            number[b] = 1

        union(a, b)

        print(number[find(b)])
