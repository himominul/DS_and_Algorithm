#Linear Search pseudoCode :
"""
1. Traverse the Array - (loop)
1. if array[index] == findvalue:
        print(value found)
        exit;
3. if not found in array :
        print(not found)
"""

def linear_search(list,findvalue):
    for i in range(len(list)):
        if list[i]==findvalue:
            print("Value Found at positon ",i)
            break
  
mList = [1,2,4,6,3,7,9,10]
mfind = 9
mSearch = linear_search(mList,mfind)
#print(mSearch)

