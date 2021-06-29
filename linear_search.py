#Linear Search pseudoCode :
"""
1. Traverse the Array - (loop)
1. if array[index] == findvalue:
        print(value found)
        exit;
3. if not found in array :
        print(not found)
"""
#Basic Function
def BLinear_search(list,findvalue):
    for i in range(len(list)):
        if list[i]==findvalue:
            print("Value Found  position at :  ",i)
            break
    else:
        print("Not Found ! ")
#Boolean flag using FUnction
def FLinear_search(mlist,findvalue):
    found = False
    for  i in range(len(mlist)):
        if mlist[i] == findvalue:
            found = True
            positon = i
            break
    if found == True:
        print("Value Found  position at :  ",positon)
    else:
        print("Value Not Found")

#Function using Conditional loop
def CLinear_search(mlist,findvalue):
    found = False
    count = 0
    while count < len(mlist) and found == False:
        if mlist[count] == findvalue:
            found = True
            postion = count
            break
        count +=1
    if found == True:
        print("Value Found  position at : ",postion)
    else:
        print("Value NOt FOund")

mList =[int(x) for x in input("Enter The Value of List : ").split()]
mfind = int(input("Enter the Find Value : "))

mSearchB = BLinear_search(mList,mfind)
mSearchF = FLinear_search(mList,mfind)
mSearchC = CLinear_search(mList,mfind)
#print(mSearch)

