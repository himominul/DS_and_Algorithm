
def bubbleSort(itemData):

    n = len(itemData)

    for i in range(0,n):

        for j in range(0,n-i-1):
           
            if itemData[j] > itemData[j+1]:
                itemData[j],itemData[j+1] = itemData[j+1],itemData[j]
                # temp = itemData[j]
                # itemData[j] = itemData[j+1]
                # itemData[j+1] = temp

    return itemData


data = [1,8,3,2,5,9,7]
b = bubbleSort(data)
print(b)


