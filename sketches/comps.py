def comps_3n2(x: list):
    aMin = x[-1]
    aMax = x[-1]
    for idx in range(0, len(x)//2):
        if x[idx*2] < x[idx*2 + 1]:
            bMin = x[idx*2]
            bMax = x[idx*2 + 1]
        else:
            bMin = x[idx*2 + 1]
            bMax = x[idx*2]
        aMin = min(aMin, bMin)
        aMax = max(aMax, bMax)
    return aMin, aMax
