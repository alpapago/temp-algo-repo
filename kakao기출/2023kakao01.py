def solution(friends, gifts):
    answer = 0
    
    # 사람 수
    n = len(friends)

    # 요소 인덱스로 번호붙이기
    idx_dic = dict()
    for idx, i in enumerate(friends):
        idx_dic[i] = idx

    # 관계 배열 하나 만듦
    # i번째 index는 준사람, j 번째 index는 받은사람
    toss = [[0]*n for _ in range(n)]
    
    # 관계도 만들기
    for gift in gifts:
        s,r = gift.split(' ')
        toss[idx_dic[s]][idx_dic[r]] += 1

    # 받은 선물 갯수
    get = [0]*n

    # 준 선물 갯수 
    send = [0]*n

    # 선물 지수 만들기
    for gift in gifts:
        sender, receiver = gift.split(' ')
        get[idx_dic[sender]] += 1
        send[idx_dic[receiver]] += 1

    # gift_idx
    gift_idx = [0]*n
    for i in range(n):
        gift_idx[i] = get[i]-send[i]

    # 받은선물 카운트
    count = [0]*n

    for i in range(n):
        for j in range(i+1,n):
            if i != j:
                # 선물 주고받은 기록이 없거나, 같을 땐
                if toss[i][j] == toss[j][i]:
                    if gift_idx[i] > gift_idx[j]:
                        count[i] += 1
                    elif gift_idx[i] < gift_idx[j]:
                        count[j] += 1
                
                elif toss[i][j] > toss[j][i]:
                    count[i] += 1
                else:
                    count[j] += 1
    
    answer = max(count)
    return answer