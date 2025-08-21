
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


