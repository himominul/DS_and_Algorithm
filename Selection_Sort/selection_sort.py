
def selectionSort( mList ):
    n = len( mList )
    for i in range( n - 1 ): 
        minValueIndex = i

        for j in range( i + 1, n ):
            if mList[j] < mList[minValueIndex] :
                minValueIndex = j

        if minValueIndex != i :

            temp = mList[i]
            mList[i] = mList[minValueIndex]
            mList[minValueIndex] = temp

    return mList

data  = [21,1,6,9,33,3,50]

print(selectionSort(data))