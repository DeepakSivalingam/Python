
# palindrome 

string="madam"

def ispalindrome(str):
    reverse=str[::-1]
    return reverse

reverse=ispalindrome(string)

if(string==reverse):
    print("palindrome")
else:
    print("not a palindrome")
    

#occurences of each character in a string
# collections is a module that provides different data structure  like
'''Counter -- Counts occurrences of elements in an iterable
'''

import collections

str="program"
print(dict(collections.Counter(str)))

or

dictionary={}
for i in  str:
    if i in dictionary:
        dictionary[i]+=1
    else:
        dictionary[i]=1

for i,frequency in dictionary.items():
    print(f"{i} : {frequency}")



#Write a program to find the longest word in a given sentence.

word=list(input("enter the sentence  : ").split(" "))
max=word[0]
for i in word:
    if len(i)>len(max):
        max=i
print(max , len(max))




# reverse a sentence without using built in functions


sentence="iuyi etiugjee etijge tio"
word=''
words_list=[]

for char in sentence:
    if char != " ":
        word += char
    else:
        words_list.append(word)
        word =""
# Append the last word
words_list.append(word)


reversed_string=""
for i in range(len(words_list)-1,-1,-1):
    reversed_string+=words_list[i]
    if i!=0:
        reversed_string+=" "
print(reversed_string)
    


#How to calculate the number of vowels and consonants in a string?

string2="PRograming".lower()
vowels=0
consonants=0
for i in string2:
    if(i>='a' and i<='z'):
        if(i=='a' or i=='e' or i=='o' or i=='u' or i=='i'):
            vowels+=1
        else:
            consonants+=1
print(vowels)
print(consonants)


#Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which number is not present in the second array.


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 1, 0, 5]

missing_numbers = []
for i in range(len(arr1)):
    found = False
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            found = True
            break
    if not found:
        missing_numbers.append(arr1[i])

print("Missing numbers:", missing_numbers)




# reverse an array
arr=[1,2,3,4,5]
start=0
end=len(arr)-1
while(start<end):
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp
    start+=1
    end-=1
print(arr)


# linear search

list=[78535,535,2,7,5]
x=2
found=False
for num in list:
    if num==x:
        print(list.index(num))
        found=True
if not found:
    print("index not found ")
    
#binary search 

list=[78535,535,2,7,5]
list.sort()

key=5
start=0
end=len(list)-1
 
def binary(list,start,end,key):
     mid=(start+end)//2
     
     if(list[mid]==key):
         print("index is found ",mid)
     elif(key<list[mid]):
         binary(list,start,mid-1,key)
     elif(key>list[mid]):
         binary(list,mid+1,end,key)
     else:
         print("index is not found ")

binary(list,start,end,key)


#bubble sort

list=[384976,3,3434,1,234]

def bubblesort(list):
    n=len(list)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if(list[j]>list[j+1]):
                list[j],list[j+1]=list[j+1],list[j]
                swapped=True
        if not swapped:
            break
    return list

print(bubblesort(list))
        

#selection sort

list=[384976,3,3434,1,234]

def selectionsort(list):
    n=len(list)
    for i in range(n):
        minindex=i
        for j in range(i+1,n):
            if list[j]<list[minindex]:
                minindex=j

        temp=list[i]
        list[i]=list[minindex]
        list[minindex]=temp
    print(list)

selectionsort(list)


#reverse a number 
num=567
reversed=0
while(num>0):
    x=num%10
    reversed=(reversed*10)+x
    num//=10
print(reversed)




#armstrong number 

num = 15
original = num   # keep a copy
count = 0
sumofnumber = 0

# Count digits
temp = num
while temp > 0:
    count += 1
    temp //= 10

# Calculate sum of digits raised to 'count'
temp = num
while temp > 0:
    x = temp % 10
    sumofnumber += x ** count
    temp //= 10

# Compare with original number
if original == sumofnumber:
    print("Armstrong")
else:
    print("Not an Armstrong")



#anagaram

from itertools import permutations

def is_anagram_bruteforce(s1, s2):
    # Step 1: If lengths are not same, they can't be anagrams
    if len(s1) != len(s2):
        return False
    
    # Step 2: Generate all permutations of s1
    for perm in permutations(s1):
        # Step 3: Convert tuple (e.g., ('l','i','s','t','e','n')) to string
        if ''.join(perm) == s2:
            return True
    
    # Step 4: If no match found, return False
    return False

# Example usage
print(is_anagram_bruteforce("listen", "silent"))  # True
print(is_anagram_bruteforce("hello", "bello"))    # False



#automorphic number 

num=int(input("enter the number "))
square =num*num

if(str(square).endswith(str(num))):
    print("automorphic number ")
else:
    print("not an automorphic number ")


#binary to decimal 

# Convert binary to decimal using int() function
binary = input("Enter a binary number: ")
decimal = int(binary, 2)
print(f"Decimal equivalent: {decimal}")

or

# Convert binary to decimal manually
binary = input("Enter a binary number: ")
decimal = 0
power = 0

# Start from the rightmost digit
for digit in reversed(binary):
    decimal += int(digit) * (2 ** power)
    power += 1

print(f"Decimal equivalent: {decimal}")


#decimal to binary 

# Convert decimal to binary using bin()
decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]  # [2:] removes the '0b' prefix
print(f"Binary equivalent: {binary}")

or 

# Convert decimal to binary manually
decimal = int(input("Enter a decimal number: "))
binary = ""

if decimal == 0:
    binary = "0"
else:
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary  # prepend remainder
        decimal //= 2

print(f"Binary equivalent: {binary}")


# check valid binary number 

binary_str = '1010101089710'
flag = True  # Assume it is binary unless proven otherwise

for i in binary_str:
    if i != '0' and i != '1':  # Check if any character is not 0 or 1
        flag = False
        break  # No need to check further if an invalid digit is found

if flag:
    print("Valid binary number")
else:
    print("Not a valid binary number")


#duck number 

num=input("enter the number ")
duck=False
for i in num:
    if i=='0' and ( not num.startswith('0')):
        duck=True

if(duck):
    print("duck number ")
else:
    print("not a duck number ")


#happy number 

def is_happy(num):
    seen = set()  # to detect cycles

    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))

    return num == 1


# Driver code
n = int(input("Enter a number: "))
if is_happy(n):
    print(f"{n} is a Happy Number")
else:
    print(f"{n} is not a Happy Number")


#harshad number 
num=int(input("enter the number "))
sum=0
nums=num
while num>0:
    temp=num%10
    sum+=temp
    num//=10

if(nums % sum==0):
    print("harshad number ")
else:
    print("not a harshad number ")



#magic number 

def is_magic(num):
    while num > 9:  # repeat until we get a single digit
        s = 0
        while num > 0:
            s += num % 10  # add last digit
            num //= 10      # remove last digit
        num = s  # assign the sum back to num
    
    return num == 1


# Driver code
n = int(input("Enter a number: "))
if is_magic(n):
    print(f"{n} is a Magic Number")
else:
    print(f"{n} is not a Magic Number")



