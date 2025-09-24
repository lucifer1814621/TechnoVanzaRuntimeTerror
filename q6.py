s=int(input("enter number of silver coins:"))
g=int(input("enter  number of Gold coins:"))

if s>50 or g>5:
    print("Rich Tax")

elif s<10 and g==0:
    print("Pass Free!")

else:
    print("Normal Tax")