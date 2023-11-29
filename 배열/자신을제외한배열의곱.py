nums = [1,2,3,4]

def mul(nums:list[int])->list[int]:
    p = 1
    out = []

    # 왼쪽에서 곱해서 out에 저장
    for i in range(len(nums)):
        out.append(p)
        p = p*nums[i]

    print(out)

    # 오른쪽부터 돌면서 out값이랑 저장
    p = 1
    for i in range(len(out)-1,-1,-1):
        out[i] = out[i]*p
        p = p*nums[i]

    return out

print(mul(nums))