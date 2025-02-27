def solution(info, n, m):
    stuff = {0: 0}

    for a, b in info:
        new_stuff = dict()
        for aa, bb in stuff.items():
            if a + aa < n:
                new_stuff[a + aa] = min(new_stuff.get(a + aa, bb), bb)
            if b + bb < m:
                new_stuff[aa] = min(new_stuff.get(aa, b + bb), b + bb)
        stuff = new_stuff

    return min(stuff.keys()) if stuff else -1