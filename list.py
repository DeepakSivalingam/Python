# mutable
# collection of data with different data type 
#we can perform the slice operation in list .. it is mutable

a=[2,6.0,"deepak"]
print(a)
print(type(a))
print(a[::-1])
print(a[-1])

a[1]=3
print(a)

#nested list 
a=[2,6.0,"deepak",[2,'hii',0.5]]
print(a[3][2])

print("--------------------------------------------------------------------")
# list functions 

list=[2,0.8,'hiii',8,9.3,'welcome']
print(list.clear())  #to clear the list values 

list=[2,0.8,'hiii',8,9.3,'welcome']
list1=list.copy()
print(list1)

list=[2,0.8,2,2,'hiii',8,9.3,'welcome']
print(list.count(2))  #return the number of times the value is exist in the list 

list=[2,0.8,2,2,'hiii',8,9.3,'welcome']
print(list.index(2))  #return the index of the given value 

list=[2,0.8,2,2,'hiii',8,9.3,'welcome']
print(len(list))  # return the length of the list 

list2=[2,0.8,2,2,8,9.3]
print(max(list2))   # return the maximum and minimum value in the list 
print(min(list2))
print(sum(list2))

list2=[2,0.8,2,2,8,9.3]
list2.pop(0) # remove the values in the list based on the index position 
print(list2)


list2=[2,0.8,2,2,8,9.3]
list2.remove(2)  # removes the values in the list based on the values
print(list2)

x=[2,4]
x.append(6)
x.append("hiiiiiii")  # append the single values 
print(x)

y=[4,9,0,0.4]
x.extend(y)    # to join the two list 
print(x)

x.insert(2,7)  # insert the values into the list by  providing the index where to insert ...first parameter tells about the index value
print(x)

y=[4,9,0,0.4]
y.sort()       # to sort the list  in ascending order ..it also applicable for string values 
print(y)
y.sort(reverse=True)  # to sort the list in descending order 
print(y)





