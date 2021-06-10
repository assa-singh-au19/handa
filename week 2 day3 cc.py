print("enter ist no.a")
a=int(input())
print("enter the second no.b")
b=int(input())
print("enter the third no.c ")
c=int(input())

if a>b and a>c:
    print("a no. is maximum no.", a)
elif b>a and b>c:
    print("b no. is maximum no.", b)
elif c>a and c>b:
    print("c no. is maximum no.", c)
else:
    print("no. is equal")
