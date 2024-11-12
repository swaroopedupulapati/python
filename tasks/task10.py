"""
convert the following functions into anonymous functions
"""
def homepage(name, bank):
    return f"Hey {name}, Happy {bank} Banking"
homepage("akki","sbi")

def isNegative(num):
    return num<0

def multiply(n1, n2, n3=1):
    return n1*n2*n3

def check(num):
    return num > 0 and num != 4

home=lambda name,bank:f"Hey {name}, Happy {bank} Banking"
print(home("akki","sbi"))

neg=lambda num:num<0
print(neg(6))

mul=lambda n1, n2, n3=1:n1*n2*n3
print(mul(10, 2 ,5))

check = lambda num:num > 0 and num != 4
print(check(3))