'''#/n--new line

//in python there is no concept of primitive and non primitive data types ...all data types considered as objects 

print("hello world")
a=10
b=20
c=a+b
print("total:",c)
print(type(a))# data type
print(id(a))# it memory location...memory location can be depends on the values.if the value of two variable is same then its memory location could be same


#keyword
# keyword are reserved words.they are cannot be used as variable name ,function name or identifier.case sensitive
# 35 keywords

    import keyword
    print(keyword.kwlist)

    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

    #getting inputs from user
    name=input("enter your name :") #normally the input statement specifies the string datatype
    print(name)

# one way
x=int(input("enter the value of x: "))
y=float(input("enter the value of y: "))
z=x+y
print(z)

#second way
fname,lname=input("enter the fname and lname : ").split('.')
print(fname +"."+lname)

#multiline string getting as a input 
string=""" 
           the Europeans in India and the British consolidation of power
in India besides incorporating additional information under
several chapters. There are also chapters on the challenges
that a newly independent nation faced in the wake of a brutal
partition. The Nehruvian era is also briefly discussed. The
chapter on India after Nehru discusses various developments
under the governments that came after 1964. In the Appendices,
a survey of personalities associated with various movements
is given.

"""
print(string)'''


# single line comment


#print parameters 

print('a',"b",sep='&',end='hi')
file1=open("sample file.txt","w")
print("this is the file ",file=file1)
file1.close()
  
name="deepak"
print("name is " +name)


-----------------------------------------------------Data types------------------------------------


1.Numeric Types

int → integers

float → decimals

complex → complex numbers

a = 10          # int
b = 3.14        # float
c = 2 + 3j      # complex

2. Sequence Types

str → string

list → ordered, mutable collection

tuple → ordered, immutable collection

text = "Hello"            # string
nums = [1, 2, 3]          # list
coords = (10, 20)         # tuple

3. Set Types

set → unordered collection of unique elements

frozenset → immutable set

s = {1, 2, 3, 2}          # {1, 2, 3}
fs = frozenset([1, 2, 3]) # immutable

4. Mapping Type

dict → key-value pairs

student = {"id": 101, "name": "Deepak", "cgpa": 9.0}

5. Boolean Type

bool → True or False

is_active = True
is_admin = False

6. None Type

None → represents null/empty value

x = None

🔍 Checking Data Type

Use type() function:

print(type(10))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("Deepak"))   # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>







  
