import sympy

for row in range(1,4):
    list1 = []
    for col in range(1,4):
        num = sympy.randprime(2,100)
        list1.append(num)       
    print(list1)
