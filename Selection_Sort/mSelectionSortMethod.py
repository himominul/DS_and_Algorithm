
#Finde THe Smallest Index
def findSmallest(arr):
    smallest = arr[0]
    min_index = 0

    for i in range (1,len(arr)):
       if arr[i] <smallest:
            smallest = arr[i]
            min_index = i

    return  min_index

#list SelectionSort
def selectionSort(arr):

    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))

        #a = print(newArr)
    return newArr

def line():
    a = print('--------------------')
    return a

print("Before Sorting List")
line()
data =[1,5,2,7,8,6]
print(data)
line()
print("After  Sorting List")
line()
print(selectionSort(data))

line()

print("\nBefore Sorting List")
line()
data2 =[10,50,70,30,20,5] 
print(data2)
line()
print("After  Sorting List")
line()
print(selectionSort(data2),"\n")
