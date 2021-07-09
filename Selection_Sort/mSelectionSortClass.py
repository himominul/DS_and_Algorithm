

class SelectionSort:

    def __init__(self):
        self.item = []

    def findSmallest(self,arr):
        smallest = arr[0]
        min_index = 0
        
        for i in range (1,len(arr)):
            if arr[i] <smallest:
                smallest = arr[i]
                min_index = i

        return  min_index

#list SelectionSort
    def selectionSort(self,arr):
        
        newArr = []
        for i in range(len(arr)):
            smallest = self.findSmallest(arr)
            newArr.append(arr.pop(smallest))

        a = print(newArr)
        return a


    def line(self):
        a = print('--------------------')
        return a


