arr = [2,1,8,12,34,15,45,56,57,78]
#Random access
print(arr[4])
## Search for an element "15" and if it's present in an array, return the index of that element
##if the searching elemnt is not present in an array, return -1 

def linearSearch(arr, x):
    for i in range(len(arr)):            ## Time commplexity O(n)
        if arr[i] == x:
            return i
    return -1
x=25                ##Linear Search
result = linearSearch(arr,x)
print("Searchihg element is present at the index" ,result)


## Insert an element 100 at index 2
arr.insert(2, 100)
arr.pop(6)
arr.sort()
print(arr)     ##O(n)















































































































































































