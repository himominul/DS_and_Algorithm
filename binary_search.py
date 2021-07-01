
# Binary search psudocode:
"""
1. array will be sorted.
2. mid = (low +high)2
3. if ( find == array[mid])
        return mid
4. else if (find > array[mid]): // search in right side
        low = mid +1
5. else://search in left side.
        high = mid -1

"""

"""
## Two way we implement the Binary search

        1. Iterative Method
        2. Recursive Method

"""
#Binary Search Implementation

# 1. Iterative Method
def binary_search(mList,findValue):
    
    low = 0
    high = len(mList)-1

    for i in range(len(mList)):
        
        mid = ((low + high) // 2)
        if findValue == mList[mid]:
            return mid 

        elif findValue > mList[mid]:
            low = mid + 1
        
        else:
            high = mid -1 
    return -1


# 2. Recursive Method
def rec_binary_search(mList,low,high,findValue):

    if high >= low: 
        mid = ((low +high) //2) 
    
        if findValue == mList[mid]:
           return mid

        elif mList[mid] > findValue:
            #low = mid + 1
            return rec_binary_search(mList,low,mid-1,findValue)            
        else:
            #high = mid -1 
            return rec_binary_search(mList,mid+1,high,findValue)
    else:
        return -1


# itrative Medhod...    
def wbinary_search(mList,mFindValue):
    low = 0
    high = len(mList) - 1
    while low <=  high:
    
        mid = (low + high) // 2
        gess = mList[mid]
        if gess == mFindValue:
            return mid       
        elif gess > mFindValue:
            high  = mid - 1
        else :
            low = mid +1

    return -1

#-------------------------------#

mList =[int(x) for x in input("Enter The Value of Sorted List  : ").split()]
mfind = int(input("Enter the Find Value : "))


search = binary_search(mList,mfind)
wsearch = wbinary_search(mList,mfind)
reSearch = rec_binary_search(mList,0,len(mList)-1,mfind)

if wsearch and search and reSearch and reSearch != -1:
    print('\n--- Iterative Method ---')
    print("Element found at index : ",str(wsearch))
    print("Element found at index : ",str(search))
    print('\n--- Recurcive Method ---')
    print("Element found at index : ",str(reSearch),"\n")

else:
    print("\n Opps! Element  is not Found \n ")
