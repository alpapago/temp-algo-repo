n = int(input())

row = [0] * (n)  # col값 저장


def check(r):
    for i in range(r):
        if row[i] == row[r]:
            return False
        if abs(row[r] - row[i]) == r - i:
            return False
    return True


result = 0


def dfs(r):
    global result
    if r == n:
        result += 1
    else:
        for c in range(n):
            row[r] = c
            if check(r):
                dfs(r + 1)


dfs(0)
print(result)
