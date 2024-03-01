def romantoInt(a):
    d = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    prev = 'I'
    result = 0
    for curr in a[::-1]:
        if (d[curr] < d[prev]):
            result = result - d[curr]
        else:
            result = result + d[curr]
        prev = curr
    return result

print(romantoInt("XXXIV"))