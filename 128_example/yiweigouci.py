"""
易位构词

1. 遍历单词列表
    每一个单词按字母排序
    将排序好的新单词作为键，原单词索引作为值建立字典（签名）

2. 遍历单词字典
    如果新单词对应值的数量大于1 （忽略没有易位构词的词）
    遍历原单词索引构建结构数组
"""

def anagrams(w):
    w = list(set(w))
    d = {}

    for i in range(len(w)):
        s = ''.join(sorted(w[i])) # 签名
        if s in d:
            d[s].append(i)
        else:
            d[s] = [i]
    
    # -- 提取易位构词
    response = []
    for s in d:
        if len(d[s]) > 1:      # 忽略没有易位构词的词
            response.append([w[i] for i in d[s]])
    return response

if __name__ == "__main__":
    v = anagrams(['le', 'chien', 'marche', 'vers', 'sa', 'niche',
                  'et', 'trouve', 'une', 'limace', 'de', 'chine',
                  'nue', 'pleine', 'de', 'malice', 'qui', 'lui',
                  'fait', 'du', 'charme'])
    print(v)