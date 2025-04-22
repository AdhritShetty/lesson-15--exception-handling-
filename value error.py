try:
    n=int(input("enter a number:"))
except ValueError as ex:
    print("exception:",ex)
print("you are outside the try block")

 