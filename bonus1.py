n=int(input("Enter number of bulbs: "))
p=int(input("Enter number of pass toggled: "))

if n>0:
   

    if p==1:
        print("Every Bulb is ON.")

    elif p==2:
        for i in range(1,n+1):
         if i//2==i/2:
            print(i,"on")

         elif i//2!=i/2:
            print(i,"OFF")

    elif p==3:
        for i in range(1,n+1):
            if i//3==i/3:
                print(i,"on")

            elif i//3!=i/3:
                print(i,"OFF")

    else:
        print("Enter a valid pass!")

else:
    print("Enter A valid number of bulbs.")
