#programmet ska konvertera USAs miles/gallons till km/liter
miles = float(input('hur många miles har din bil åkt?')) # konverterar mumret man skrivet ut till datatypen float 
gallon = float(input('hur många gallons av bensin har din bil använt? ')) #samma som 2an
km = miles * 1.609 #tar värdet som getts om miles och omvandlar det till km
liter = gallon * 3.785 #samma som 4n fast men gallon och liter
print(f'din bil har åkt {km:.2f} km') #printar ut det slutliga värdet med en text som beskriver att det är i km nu och har bara högst 2 decimaltal
print(f'din bil har använt {liter:.2f} liter')#samma som 6an men med liter