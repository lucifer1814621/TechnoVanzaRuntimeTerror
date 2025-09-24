a=str(input("Enter the word: "))
b=[]
c=[]


for i in a:
    
    b.append(i)

for ki in a:
    
    c.append(ki)
    

b.reverse()


if b==c:
    print("The word is mirrored")

else:
    print("The word is different when mirrored")