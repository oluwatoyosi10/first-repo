
print("you get a 8")
studentGrade = int(input("Enter a score: "))
if studentGrade >= 80:
    print("you got A")
elif studentGrade >= 70:
    print("you get a b ")
elif studentGrade >= 60 :
    print("you get a c")
elif studentGrade >= 50:
    print("you get a d")
elif studentGrade >= 40:
    print("you get a e")
else:
    print("you get an f")



#buiding a calculator
#num1
#num2
#operation +-/*
#result




temp = float(input("what is the temperature"))
tempd = input("is it in calcius or fahrenheit: ")
if tempd == "c":
    f = temp * 9 / 5 + 32
    print(f)
elif tempd == "f":
    c = (temp - 32) * 5 / 9
    print(c)


