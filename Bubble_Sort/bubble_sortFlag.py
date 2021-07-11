
def bubbleSort(dataSet):

    n = len(dataSet)
    for i in range(n):
        flag = True
        print('\ni-----%d'%i)
        for j in range (n-i-1):
            print('j-----%d == '%j,dataSet[j])

            if dataSet[j] > dataSet[j+1]:

                dataSet[j],dataSet[j+1] = dataSet[j+1],dataSet[j]

                flag = False

        if flag == True:
            break

    return dataSet


dataSet = [1,2,3,4,5,7,6]
print(bubbleSort(dataSet))
