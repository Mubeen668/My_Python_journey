# vowels count with loops
str = input()
str2=str.lower()
count=0
vow ="aeiou"
for i in str2:
    if i in vow:
        count+=1
print(count) 

# vowels count with generator expression
s = "hello world"
vowels = 'aeiou'
count = sum(1 for char in s if char in vowels)
print("Vowels:", count)