def max_element(lst):
    n = len(lst)
    maxElement = 0
    for i in range(0,n):
        if(lst[i]>maxElement):
            maxElement = lst[i]
    return maxElement
    
def find_mode(lst):
    n = len(lst)
    maxElement = 0
    mode = lst[0]
    for i in range(0,n):
        if(lst[i]>maxElement):
            maxElement = lst[i]
            mode = i
            
    return mode

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
    biggest = max_element(lst)
    countArr = [0]*(biggest+1)
    outArr = [0]*(n)
    
    for i in range(0,n):
        element = lst[i]
        countArr[element] = countArr[element]+1
    
    mode = find_mode(countArr)
    
    
    cummulative_sum(countArr)
    
    i = n-1
    while i > -1:
        outArrIdx = countArr[lst[i]] -1
        print("outArrIdx: " + str(outArrIdx))
        print("element: " + str(lst[i]))
        outArr[outArrIdx] = lst[i]
        countArr[lst[i]] = outArrIdx
        i =i-1
    return mode,outArr

def find_median(arr):
    
    mode,arr = counting_sort(arr)
    
    n = len(arr)
    
    if(n%2 == 0):
        median = (arr[n//2] + arr[ (n//2)-1])/2
    else:
        median = arr[(n-1)//2]
        
    
    return mode,median,arr
    
    
if __name__ == "__main__":
    list=[5,2,8,1,4,9,5,6,9,0,9]
    print("unsorted array")
    print("**************************************")
    print(list)
    mode, median, sorted_arr = find_median(list)
    print("**************************************")
    print("Mode : " + str(mode))
    print("Median : " + str(median))
    print("Sorted array using counting sort")
    print(sorted_arr)