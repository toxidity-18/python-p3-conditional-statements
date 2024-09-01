
# Python
#if and if else statements
dog = "cuddly"

if dog == "hungry":
    owner = "Refilling food bowl."
elif dog == "thirsty":
    owner = "Refilling water bowl."
elif dog == "playful":
    owner = "Playing tug-of-war."
elif dog == "cuddly":
    owner = "Snuggling."
else:
    owner = "Reading newspaper."
    #any value which is empty or zero is falsy value
    #use of cnditional expressions
    #ternary expressions
    #how to write conditional expressions
    age = 0
    if age > 0:
        print("yep!")
    else:
        print("nope!")
    #which also euialent to this 
    print("yep!" if age > 0 else "nope!")
    #try/expect -use of finaly keywords
def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally:
        print("Isn't division fun?")
#switch and cae statement in python