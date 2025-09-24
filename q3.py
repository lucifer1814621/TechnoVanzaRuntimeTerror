x=int(input("enter a number:"))
y=int(input("enter another number:"))
z=int(input("enter another number:"))

if x+y==z:
    print("Proceed!")

elif x+z==y:
    print("Proceed!")

elif x==y+z:
    print("Proceed!")

else:
    print("HALT!")