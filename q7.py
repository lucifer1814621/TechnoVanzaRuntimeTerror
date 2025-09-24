s=int(input("enter your score:"))
r=int(input("Do you have a special reccomendation? (Type 1 for yes and 0 for no)"))

if r==1:
    if s>50:
        print("You are eligible!")

    elif s==100:
        print("You are a master!")

    else:
        print("You are not eligible!")

elif r==0:
    if s>70:
        print("You are eligible!")

    elif s==100:
        print("You are a master!")

    else:
        print("You are not eligible!")

elif s<50:
    print("You are not eligible!")

else:
    print()
