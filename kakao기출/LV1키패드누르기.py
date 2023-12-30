num = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
han = 'right'

def solution(numbers, hand):
    pos = dict()
    pos[0] = (1,3)
    left = (0,3)
    right = (2,3)
    
    dx = 0
    dy = 0
    for i in range(1,10):
        if i%3 == 1 and i!=1:
            dx = 0
            dy += 1
        pos[i] = (dx,dy)
        dx += 1

    answer = ''
    
    for i in numbers:
        px, py = pos[i]

        if i in [1,4,7]:
            answer += 'L'
            left = (px,py)
        elif i in [3,6,9]:
            answer += 'R'
            right = (px,py)
        else:
            # 왼손이랑 떨어진 거리 구하기
            dl = abs(left[0]-px)+abs(left[1]-py)

            # 오른손이랑 떨어진 거리 구하기
            dr = abs(right[0]-px)+abs(right[1]-py)

            # 둘이 거리 차 비교하기!
            # 거리가 같다면?
            if dl == dr:
                # 거리 똑같은데, 오른손잡이라면?
                if hand == 'right':
                    answer += 'R'
                    right = (px,py)
                # 거리 똑같은데, 왼손잡이라면?
                elif hand == 'left':
                    answer += 'L'
                    left = (px,py)
            # 오른손이 더 가까이에 있다면?
            elif dl > dr :
                answer += 'R'
                right = (px,py)
            # 왼손이 더 가까이에 있다면?
            else:
                answer += 'L'
                left = (px,py)
            
    return answer

print(solution(num,han))