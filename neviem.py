a=int(input("Zadaj cislo a"))
b=int(input("Zadaj cislo b"))
c=int(input("Zadaj cislo c"))
if c>a and a>b:
    print("c,a,b")
if a>b and a>c:
    if b>c:
        print("a,b,c")
    if a>c and c>b:
        print("a,c,b")
if b>c and c>a:
    print("b,c,a")
if b>a and a>c:
        print("b,a,c")
if c>b and b>a:
        print("c,b,a")


