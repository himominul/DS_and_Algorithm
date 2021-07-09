from mSelectionSortClass import *

ss = SelectionSort()


print("\nBefore Sorting List")
ss.line()
data =[1,5,2,7,8,6]
print(data)
ss.line()
print("After  Sorting List")
ss.line()

ss.selectionSort(data)

ss.line()