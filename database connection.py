
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
