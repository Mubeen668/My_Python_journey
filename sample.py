
'''x = 42
print(type(x))           # <class 'int'>
print(isinstance(x, int))  # True'''



'''s = "123abc"
try:
    n = int(s)
except ValueError:
    print("Cannot convert to int")
'''
# sum of first 5 numbers 
'''n= int(input())
s=0
i=0
while i<n:  # by while loop
    s =s+i+1
    i +=1
print(s)

sum=0 
for i in range(1,n+1):  # by for loop
    sum +=i
print(sum)'''

# multiplication table 
'''n= int(input())
i=1
for i in range(1,11):
    print(f'{n}*{i} = {n*i}')
'''
# factorial program
'''n= int(input())
sum=1 
for i in range(1,n+1):  # by for loop
    sum *=i
print(sum)
'''
# sample function problem
'''def sum(x,y):
    return x+y

a,b= map(int, input().split())
print(sum(a,b))
'''
# Global scope example
''' a=5
def func():
    print(a)
func()
print(a)
'''
# Lambda function
'''sum = lambda x,y: x+y
a,b= map(int,input().split())
print(sum(a,b))
'''
# LIST
'''
l=[1,3,2,"pandu",4]
l2=[7,8]
l.remove(2)
l.append("geethu")
l.insert(2,"mubeen")
l.extend(l2)
l.reverse()
print(l)
'''
#maximum and minimum without built in functions
'''l = [10,20,3,440,50]
max=l[0]
min=l[0]
for i in l:
    if i>max:
        max=i
    if i< min:
        min=i
print(max,min)
'''
#l=[4,2,4,53,7]
#l.sort()
#print('minimum',l[0],'maximum',l[-1])

# count the occurence of a particular number from the list
'''
l = input().split()
li = [int(i) for i in l]
n = int(input())

# method 1: Using count() method
print(li.count(n))

# method 2: Using list comprehension
print(sum(1 for i in li if i == n))
'''
# second largest number in the list
'''
n = int(input())
arr = list(set(map(int, input().split())))
print(arr.sort())
print(arr[-2])
'''

#result = [x**2 if x % 2 == 0 else x for x in range(1, 11)]
#print(result)




