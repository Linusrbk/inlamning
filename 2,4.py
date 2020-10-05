#programmet ska konvertera USAs miles/gallons till km/liter
a = float(input('konvertera från miles till kilometer som din bil har åkt[1] eller konvertera från gallons till liter för hur mycket bensin har använts[2]:'))
if a == 1: 
    miles = float(input('hur många miles har din bil åkt?')) # konverterar mumret man skrivet ut till datatypen float
    km = miles * 1.609 #tar värdet som getts om miles och omvandlar det till km
    print(f'din bil har åkt {km:.2f} km') #printar ut det slutliga värdet med en text som beskriver att det är i km nu och har bara högst 2 decimaltal
elif a == 2:
    gallon = float(input('hur många gallons av bensin har din bil använt? ')) #samma som 2an
    liter = gallon * 3.785 #samma som 4n fast men gallon och liter
    print(f'din bil har använt {liter:.2f} liter')#samma som 6an men med liter
else:
    print('STOP RIGHT THERE, CRIMINAL SCUM!')
    print('YOU VIOLATED THE LAW!')
    print('PAY THE COURT A FINE OR SERVE YOUR SENTENCE!')