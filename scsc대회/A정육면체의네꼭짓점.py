T = int(input())

p = {
    0: (0, 0, 0),
    1: (0, 0, 1),
    2: (0, 1, 0),
    3: (0, 1, 1),
    4: (1, 0, 0),
    5: (1, 0, 1),
    6: (1, 0, 0),
    7: (1, 1, 1),
}
unit = [(0, 0, 1), (1, 0, 0), (0, 1, 0)]


def make_v(p1, p2):
    new = (p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])
    return new


for _ in range(T):
    # 입력받기
    gets = list(map(int, input().split()))
    gets.sort()

    ps = []
    # 두 점 조합
    ps.append(make_v(p[gets[1]], p[gets[0]]))
    # 또 다른 점
    ps.append(make_v(p[gets[3]], p[gets[2]]))

    if ps[0] in unit and p[1] in unit and ps[0] == ps[1]:
        print("YES")
    else:
        print("NO")
