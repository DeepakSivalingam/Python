'''#/n--new line

print("hello world")
a=10
b=20
c=a+b
print("total:",c)
print(type(a))# data type
print(id(a))# it memory location...memory location can be depends on the values.if the value of two variable is same then its memory location could be same


#keyword
# keyword are reserved words.they are cannot be used as variable name ,function name or identifier.case sensitive
# 36 keywords

    import keyword
    print(keyword.kwlist)

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
print("name is ",name)
  