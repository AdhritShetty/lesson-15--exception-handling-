try:
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    result=num1/num2
    print("the result is",result)

except ZeroDivisionError:
    print("it isn't allowed to use zero for division")

except NameError:
    print("it isn' allowed to write a name for division")

except:
    print("there seems to be an issue")

finally:
    print("We'll get back on it")
