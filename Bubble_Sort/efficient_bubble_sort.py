

def bubbleSort(itemData):
    sum = 0
    cnt = 0
    cnt2 = 0
    n = len(itemData)
    print('n---',n)
    for i in range(0,n):
        print('\ni---:%d '%i)
        cnt2 += 1
        for j in range(0,n-i-1):
            print('j---%d -'%j,"=== ",itemData[j])
            if itemData[j] > itemData[j+1]:
                itemData[j],itemData[j+1] = itemData[j+1],itemData[j]
                # temp = itemData[j]
                # itemData[j] = itemData[j+1]
                # itemData[j+1] = temp
            a1= itemData[n-1]
            a2 = itemData[n-2]
            cnt += 1
            

        if a1 > a2:
            break
    print("Total Loop",cnt+cnt2)
    print(a1,a2)            
              
    return itemData


data = [10,20,30,40,50,70,60]
print(bubbleSort(data))
