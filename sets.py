#it is the collection of unordered and unindexed values 
#here values cant be change but we can  insert and remove the values 
# duplicate values can be removed 


example={2,0.4,'deepak'}  # it could change the values 
print(type(example))
print(example)

# accesing the values in the set 
for i in example:
    print(i)
    
example.add(5.7)
example.add('kumar')  #values inserted in the set 
print(example)

x={2,9,0,'welcome'}   #joining of two sets
y={2,6}
y.update(x)
print(y)

y.remove('welcome')  # it can remove the values and if the values is not in the set then it throws a exception 
print(y)
y.discard('welcome')   # it can remove the values and if the values is not in the set then it leaves it 
print(y)


y.pop()     #it removes the last values in the set 
print(y)

y.clear()    # to clear the all values in the set 
print(y)

# union 
a={2,0.2,5,8,'set'}
b={0,'union'}      #its similiar to update 
print(a.union(b))

#intersection 
x={1,2,3,4,5,6}
y={5,6,7,8,9,10}
print(x.intersection(y))

#symmetric_difference.
x={1,2,3,4,5,6}
y={5,6,7,8,9,10}
print(x.symmetric_difference(y))

print(x.isdisjoint(y))
print(x.issubset(y))

