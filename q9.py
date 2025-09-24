i=int(input("Enter your annual income in gold coins: "))
t=0


if i>1000:
    print("You tax is 20%")
    t=i*0.20
    print(t)

elif i<1000 and i>500:
    print("You tax is 15%")
    t=i*0.15
    print(t)

elif i>0 and i==500:
    print("You tax is 10%")
    t=i*0.10
    print(t)
    
else:
    print("No tax!")