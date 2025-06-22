def Solution(arr):
    for x in range(len(arr)):
        min = arr[x]
        z = x
        for y in range(x,len(arr)):
            if arr[y] < min:
                min = arr[y]
                z = y
        temp = arr[x]
        arr[x] = min
        arr[z] = temp
    return arr
l = [3,4,6,1,6,16,1,7,4]
l2 = Solution(l)
print(l2)
