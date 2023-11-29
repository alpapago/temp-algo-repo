import collections

words = ['eat','tea','tan','ate','nat','bat']

def anagram(words:list[str])->list[list[str]]:
    word_map = collections.defaultdict(list)

    for word in words:
        # print(sorted(word))
        word_map[''.join(sorted(word))].append(word)
        
    # ans = []
    # for key,value in word_map.items:
    #     value.sort()
    #     ans.append(value)
    # 여기를 , list(word_map().values()) 로 한번에 처리 가능
    
    return list(word_map.values())

print(anagram(words))    
