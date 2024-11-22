list_1=[1,2,3,4,5]
print("list1",list_1)
list_2=[6,7,8,9,10]
print("list2",list_2)
list_3=list_1+list_2
print("list3",list_3)
even_list= []
odd_list=[]
for i in list_3:
    if i%2==0:
      even_list.append(i)
    else:
      odd_list.append(i)
even_list.sort()
odd_list.sort()
d=even_list+odd_list
print("sorted order",d)

