age=int(input("Please enter your age in years: "))

if age<18:
    print("You are a minor.")

elif age==25:
    a=int(input("Do you have a Royal decree? (Type 1 for yes and 2 for no)"))
    if a==1:
        print("Nobel")
    else:
        print("You are an adult!")

elif age>=18 and age<=65:
    print("You are an adult!")

else:
    print("You are an elder!")