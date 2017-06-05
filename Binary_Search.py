#find a element in an sorted array using binary search
def binary_search(arr, l, r, x):
    if r >= l:
        mid = int((l+r) /2)
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            l = mid + 1
            return binary_search(arr, l, r, x)
        else:
            r = mid - 1
            return binary_search(arr, l, r, x)
    else:
        return -1



#arr = [1, 2, 3, 4, 5]

print("no of elements to enter")
n = int(input())
arr = list()
for i in range(0,n):
    num = int(input())
    arr.append(num)
print (arr)

while True:
    
        print ("element to find")
        x = input()
        if x == "":
            continue
        result = binary_search(arr, 0, len(arr)-1, int(x))
        if result == -1:
            print (str(x) + " not found")
        else:
            print ("Element is present at index "+str(result))
    