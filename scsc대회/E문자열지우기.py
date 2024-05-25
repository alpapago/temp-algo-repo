# 받은 문자열
s = input()


def check_front(x):
    first = x[0]
    for i in range(1, len(x)):
        if x[i] == first:
            x.pop(i)
        else:
            break
    return x


def check_back(h):
    back = h[0]
    for i in range(len(h) - 1, 0, -1):
        if h[i] == back:
            h.pop(i)
        else:
            break
    return h


def check_question(q):
    cnt = 0
    for i in range(len(q)):
        if q[i] == "?":
            cnt += 1
    return cnt


flag = True
change = 0

# 문자열 1개 : 상대가 이김
if len(s) == 1:
    if s == "?":
        flag = False
else:
    after_f = check_front(s)
    if len(s) != len(after_f):
        change += 1
    after_b = check_back(after_f)
    if len(after_f) != len(after_b):
        change += 1

    cnt_of_q = check_question(after_b)

    change += cnt_of_q

    if change % 2 == 0:  # ? 짝수개
        flag = True
    else:
        flag = False

if flag:
    print("1")
else:
    print("0")
