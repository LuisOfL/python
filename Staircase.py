def Staircase(n,dic={}):
    if n in dic:
        return dic[n]
    if n <= 1:
        return 1
    dic[n] = Staircase(n-1,dic) + Staircase(n-2,dic)
    return dic[n]

h = 4
print(Staircase(h))
