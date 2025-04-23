try:
    age1=int(input("enter your age:"))
    n=int()
    if age1%2==0:
        print("the age is even")
        print("the age is valid")
    else:
        print("the number is odd")
        print("the age is valid")
except ZeroDivisionError:
    print("an infant can't partipate in this programme")

except age1<0:
    print("negative numbers cannot be used as an age")



