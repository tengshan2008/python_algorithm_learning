from string import ascii_letters

class Trie_Node(object):
    def __init__(self):
        self.isWord = False
        self.s = {c: None for c in ascii_letters}

def add(T, w, i=0):
    if T is None:
        T = Trie_Node()
    if i == len(w):
        T.isWord = True
    else:
        T.s[w[i]] = add(T.s[w[i]], w, i + 1)
    return T

def Trie(S):
    T = None
    for w in S:
        T = add(T, w)
    return T

def spell_check(T, w):
    assert T is not None
    dist = 0
    while True:
        u = search(T, dist, w)
        if u is not None:
            return u
        dist += 1

def search(T, dist, w, i=0):
    if i == len(w):
        if T is not None and T.isWord and dist == 0:
            return ""
        else:
            return None

    if T is None:
        return None

    f = search(T.s[w[i]], dist, w, i + 1)
    if f is not None:
        return w[i] + f
    if dist == 0:
        return None
    for c in ascii_letters:
        f = search(T.s[c], dist - 1, w, i)
        if f is not None:
            return c + f
        f = search(T.s[c], dist - 1, w, i + 1)
        if f is not None:
            return c + f
    return search(T, dist - 1, w, i + 1)