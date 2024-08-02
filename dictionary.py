#it does not support duplicate values 
#dont assign the same keys . it is mutable..

example={
    "name":"deepak",
    "age":20,
    "gender":"male"
}
print(example)
print(type(example))

# accesing the values 
print(example["name"])
print(example["age"])

#another  way for accessing 
print(example.get("name"))

print(example.keys())    #return the keys only 
print(example.values())   #return the values only 

print(example.items())     #return the both values and keys 

# dictionary in loops
for i in example:
    print(i ,"",example[i])
    
for i in example.values():
    print(i)
    
for i in example.keys():
    print(i)
    
    
for i,j in example.items():
    print(i,j)
    
#updating the values 

example.update({"weight":65})
print(example)

example["age"]=21
print(example)

example.pop("age")
print(example)

#example.clear()--- removes all the key value pair in the dictionary 

#nested dictionary 
users={
    
"user1": {
    "name":"deepak",
    "age":20,
    "gender":"male"
},
"user2":{
    "name":"virat",
    "age":27,
    "gender":"male"
}
    
}
print(users)
print(users.get("user1").get("age"))


# dictionary constructor

dictionary=dict(name="deepak",age=20)
print(dictionary)



