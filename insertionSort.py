def Solution(arr):
        
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr


l = [3,6,8,2,9,1,2,7,9]
l2 = Solution(l)
print(l2)
