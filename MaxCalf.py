# Dada una lista de calificaciones [7, 8, 9, 6, 10]
# Imprime el promedio y la nota más alta
def prom(lis):
    sum = 0
    for x in range(0,len(lis)):
        sum += lis[x]
    return (sum)/(len(lis))

def MaxNot(lis):
    max = 0
    for x in range(0,len(lis)):
        if max<lis[x]:
            max = lis[x]
    return max

list = [7,8,9,6,10]
print(prom(list))
print(MaxNot(list))


