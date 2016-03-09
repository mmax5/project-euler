__author__ = 'mikemax'

P_C = {}

i = 0
while True:
    cube = i**3
    key = ''.join(sorted(str(cube)))
    if key not in P_C:
        P_C[key] = [cube]
    else:
        P_C[key].append(cube)
        if len(P_C[key]) == 5:
            print P_C[key]
            print min(P_C[key])
            break
    i += 1
