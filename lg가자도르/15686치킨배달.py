n, m = map(int, input().split())


def dist(p1, p2):
    r1, c1 = p1
    r2, c2 = p2

    return abs(r1 - r2) + abs(c1 - c2)


home = list()
chicken = list()

for r in range(n):
    tmp = list(map(int, input().split()))
    for c in range(n):
        if tmp[c] == 1:
            home.append((r, c))
        elif tmp[c] == 2:
            chicken.append((r, c))

dists = list()

for chic in chicken:
    print(chic, type(chic))
    tmp = list()
    for h in home:
        tmp.append(dist(chic, h))

    tmp.append(sum(tmp))
    dists.append(tmp)

dists = sorted(dists, key=lambda x: x[-1], reverse=True)

final = [float("inf") for _ in range(len(home))]


for distance in dists:
    if m == 0:
        break
    m -= 1

    for i in range(len(distance) - 1):
        final[i] = min(final[i], distance[i])

print(sum(final))
