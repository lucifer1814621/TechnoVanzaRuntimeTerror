x=int(input("enter a number:"))
y=int(input("enter another number:"))
z=int(input("enter another number:"))

if x==0 and y>0 and z<0:
    print("The prophecy is TRUE!")

elif x<0 and y==0 and z>0:
    print("The prophecy is TRUE!")

elif x>0 and y<0 and z==0:
    print("The prophecy is TRUE!")

else:
    print("The Prophesy is False!")