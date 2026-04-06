def merge_sorted(x, y):
    z = []
    xi, yi = iter(x), iter(y)
    x_ = next(xi, None)
    y_ = next(yi, None)
    while not (x_ is None and y_ is None):
        if y_ is None or x_ is not None and x_ <= y_:
            z.append(x_)
            x_ = next(xi, None)
        else:
            z.append(y_)
            y_ = next(yi, None)
    return z

def merge_sorted2(x, y):
    z = []
    i, j = 0, 0
    x_ = x[i] if i < len(x) else None
    y_ = y[j] if j < len(y) else None
    while not (x_ is None and y_ is None):
        if y_ is None or x_ is not None and x_ <= y_:
            z.append(x_)
            i += 1
            x_ = x[i] if i < len(x) else None
        else:
            z.append(y_)
            j += 1
            y_ = y[j] if j < len(y) else None

    return z

def merge_sorted3(x, y):
    z = []
    i, j = 0, 0
    while i < len(x) or j < len(y):
        if j == len(y) or i < len(x) and x[i] <= y[j]:
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1

    return z

if __name__ == '__main__':
    print(merge_sorted([0, 3, 5, 6], [1, 2, 4, 6, 7]))
    print(merge_sorted2([0, 3, 5, 6], [1, 2, 4, 6, 7]))
    print(merge_sorted3([0, 3, 5, 6], [1, 2, 4, 6, 7]))
