#1
def arithmetic(a, b, oper):
    if oper=="*":
        return a*b
    elif oper=="/":
        return a/b
    elif oper=="+":
        return a+b
    elif oper=="-":
        return a-b
    else:
        print("Неизвестная операция")
        return 0

#2
def is_year_leap(year):
    if (year%4==0) and (year%100!=0) or (year%400==0):
        return True
    return False

#3
from math import*
def square(a):
    P=4*a
    S=a**2
    diag=a*math.sqrt(2)
    return P, S, diag

#4
def season(month):
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"

#5
def bank(a, years):
    for year in range(years):
        a*=1.1
    return a

#6
def is_prime(number):
    if number==1:
        return False
    for possible_divisor in range(2, x):
        if (number%possible_divisor==0):
            return False
    return True

#8
def xor_uncipher(string: str, key:str)->str:
    """Kodeeritud text dekodeeritakse
    """
    result=""
    temp=[]
    for i in range(len(string)):
        temp.append(string[i])
        for j in reserved(range(len(key))):
            temp[i]=chr(ord(key[j])^ord(temr[i]))
        result+=temp[i]
    return result
