def Solution(arr):
    for x in range(len(arr)):
        for y in range(len(arr)-1-x):
            if arr[y] > arr[y+1]:
                temp = arr[y]
                arr[y] = arr[y+1]
                arr[y+1] = temp
    return arr

l = [3,4,6,1,6,16,1,7,4]
l2 = Solution(l)
print(l2)
