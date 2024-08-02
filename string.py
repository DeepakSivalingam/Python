# string 
# immutable 

# string is defined by some value that enclosed by either single or double qoutes

name="deepak "
print(name)
print(type(name))

# string functions 
str="my name is deepak"
print(str.upper())  # it makes the string to uppercase
print(str.lower())  # it makes the string to lowercase
print(str.capitalize())  # it makes the string to capitalize the first beginning of the text only 
print(str.title())     # it makes the first letter of the each word in the string to uppercase
print(str.count("a"))  # it provides the count of the particular leter in the word 
print(str.endswith("ak"))  # it returns true or false based on the what we given and then compare it to the end of the acutal string
print(str.find("a"))   # it used to find the particular letter 
print(str.find("a",6))  # here we defined the particular index for after finding the particular letter
print(str.replace("n","m"))  # here we replace the letter .first parameter leads too what the letter that we want to change  and second parameter leads to the letter to updated 
print(len(str)) #it returns the length


string="deepak"
print("isupper:",string.isupper())
print("islower:",string.islower())

s="deepak2004"
print("isalpha:",s.isalpha())
print("isalphanumeric:",s.isalnum())
print("isdigit: ",s.isdigit())

y="    hello  "
print(len(y.strip()))  # strip used for remove the unwanted white spaces
print(len(y.lstrip()))
print(len(y.rstrip()))


#string manipulation in python 

# slice operation 

example="mailam engineering college"
print(example[:])
print(example[0:])
print(example[-1])
print(example[-2:-1])
print(example[-3:-1])
print(example[:-1])
print(example[::-1]) #for reversing the string 
print(example[-2:])
print(example[2]) 