
# +

a = 21
b = 10
c = 0

tup=("+","-","*","/","%","**","//");

def prefix_func():
    return "运算符 "

print("a : "+str(a))
print("b : "+str(b))
print("c : "+str(c))
print()

for operator in tup:
    print(prefix_func()+operator)
    if(operator == "+"):
        print(a + b)
    elif (operator == "-"):
        print(a - b)
    elif (operator == "*"):
        print(a * b)
    elif (operator == "/"):
        print(a / b)
    elif (operator == "%"):
        print(a % b)
    elif (operator == "**"):
        print(a ** b)
    elif (operator == "//"):
        print(a // b)

    print("")




