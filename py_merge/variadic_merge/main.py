import heapq
def merge_sorted(*ns):
    iterated = 0
    iters = [iter(n) for n in ns]
    w, z = [], []
    for idx, it in enumerate(iters):
        n_ = next(it, None)
        if n_ is None:
            continue
        heapq.heappush(w, (n_, idx))
    while iterated != len(ns):
        t = heapq.heappop(w)
        z.append(t[0])
        n_ = next(iters[t[1]], None)
        if n_ is None:
            iterated += 1
        else:
            heapq.heappush(w, (n_, t[1]))
    return z
def merge_sorted2(*ns):
    z, w = [], []
    for n in ns:
        it = iter(n)
        while True:
            try:
                heapq.heappush(w, next(it))
            except StopIteration as err:
                break
    while len(w) != 0:
        z.append(heapq.heappop(w))
    return z


if __name__ == '__main__':
    print(merge_sorted([0, 3, 5, 6], [1, 2, 4, 6, 7], [1, 2, 4, 8, 16], [3, 9, 27]))
    print(merge_sorted2([0, 3, 5, 6], [1, 2, 4, 6, 7], [1, 2, 4, 8, 16], [3, 9, 27]))
