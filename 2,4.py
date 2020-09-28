miles = float(input('hur många miles har din bil åkt?'))
gallon = float(input('hur många gallons av bensin har din bil använt? '))
km = miles * 1.609
liter = gallon * 3.785
print('din bil har åkt', km ,'km')
print('din bil har använt', liter ,'liter')