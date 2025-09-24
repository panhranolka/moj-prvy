#7%3 zvysok po deleni
import math
a=int(input("Zadaj prvu stranu trojuholnika v cm"))
b=int(input("Zadaj druhu stranu trojuholnika v cm"))
c=int(input("Zadaj tretiu stranu trojuholnika v cm"))
if (a+b>c) and (a+c>b) and (b+c>a):
    print("je to trojuholnik")
    if (a**2+b**2==c**2) or (a**2+c**2==b**2) or (c**2+b**2==a**2):
        print("je to pravouhly trojuholnik")
    if(a==b==c):
        print("trojuholnik je rovnostranny")
    if(a==b and a!=c) or (a==c and b!=c) or (b==c and a!=c):
        print("je to rovnoramenny trojuholnik")
o = a+b+c
po = o/2
S = (po*(po-a)*(po-b)*(po-c))**0.5
va = 2*S/a
vb = 2*S/b
vc = 2*S/c
p_vpis = S/po
p_opis1 = (a*b*c)/(4*S)
alpha = round(math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c))),2)
beta = round(math.degrees(math.acos((a**2+c**2-b**2)/(2*c*b))),2)
gamma = round(math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b))),2)
print("obvod je", o ,"cm")
print("obsah je", S ,"cm")
p_opis2 = (a) / (2*math.sin(math.radians(alpha)))
print("opisana kruznica trojuhplnika je", p_opis2, "cm")
print("opisana kruznica trojuhplnika je", p_opis1, "cm")
print("vpisana kruznica je", p_vpis, "cm")
print("vyska na stranu a je", va ,"cm")
print("vyska na stranu b je", vb ,"cm")
print("vyska na stranu c je", vc ,"cm")
print("alpha je", alpha,"°")
print("beta je", beta,"°")
print("gamma je", gamma,"°")