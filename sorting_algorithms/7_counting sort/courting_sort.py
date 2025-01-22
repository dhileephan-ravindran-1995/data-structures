def max_element(lst,n):
    maxElement = 0
    for i in range(0,n):
        if(lst[i]>maxElement):
            maxElement = lst[i]
    return maxElement

def cummulative_sum(arr):
    print("countArray :")
    print(arr)
    m = len(arr)
    for i in range(0,m-1):
        arr[i+1] =  arr[i+1] + arr[i]
    print("cummulated Count Array :")
    print(arr)

def counting_sort(lst):
    n = len(lst)
    biggest = max_element(lst,n)
    countArr = [0]*(biggest+1)
    outArr = [0]*(n)
    
    for i in range(0,n):
        element = lst[i]
        countArr[element] = countArr[element]+1
    
    cummulative_sum(countArr)
    
    i = n-1
    while i > -1:
        outArrIdx = countArr[lst[i]] -1
        print("outArrIdx: " + str(outArrIdx))
        print("element: " + str(lst[i]))
        outArr[outArrIdx] = lst[i]
        countArr[lst[i]] = outArrIdx
        i =i-1
    return outArr
    
if __name__ == "__main__":
    list=[5,2,3,1,3,2,5,3,0]
    print("unsorted array")
    print("**************************************")
    print(list)
    sorted_arr = counting_sort(list)
    print("**************************************")
    print("Sorted array using counting sort")
    print(sorted_arr)