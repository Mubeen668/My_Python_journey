# simple shopping cart program

dresses = []
price  = []
total = 0 

while True:
    dress = input('enter the dress to purchase or to quite enter q: ')
    if dress.lower() =='q':
        break
    else:
        dresses.append(dress)
        price_of_dress = float(input(f'enter the price of the {dress}: $'))
        price.append(price_of_dress)

print('****** YOUR CART LIST ******')


#print(f"Your selected dresses are: {dresses[:]} ")
#print(f"Your selected dress price is: {price[:]} ")
# the above print statements can print values in list format


for dress in dresses:
    print(dress, end=' ')
print() # for new line

for p in price:
    print(p, end=' ') 
    total += p

print()
print(f"Total amount to be paid is: {total} ")
print('Thank you !')
