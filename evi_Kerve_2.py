#1
def arithmetic(a, b, r):
    if r=="+":
        return a + b
    elif r=="-":
        return a - b
    elif r=="*":
        return a * b
    elif r=="/":
        return a/b
    else:
        return "Неизвестная операция"

#2
def is_year_leap(year):

    if year % 400==0:
        return True

    if year % 4==0 and year % 100!=0:
        return True

    return False

#3
import math

def square(a):

    p = 4*a
    s = a**2
    diag=a*math.sqrt(2)

    return p, s, diag


#4
def season(month):
    if month in (12, 1, 2):
        return "зима"
    elif month in (3, 4, 5):
        return "весна"
    elif month in (6, 7, 8):
        return "лето"
    elif month in (9, 10, 11):
        return "осень"


#5
def bank(a, years):
    for year in range(years):
        a*=1.1
    return a


#6
def is_prime(number):

    if number == 1:
        return False

    for divisor in range(2, number):
        if number % divisor==0:
            return False
    return True


#7
def is_year_leap(year):

    if year % 400 == 0:
        return True

    if year % 4 == 0 and year % 100!=0:
        return True

    return False


def date(day, month, year):
    day_in_month = {1: 31,
                    2: 29 if is_year_leap(year) else 28,
                    3: 31,
                    4: 30,
                    5: 31,
                    6: 30,
                    7: 31,
                    8: 31,
                    9: 30,
                    10: 31,
                    11: 30,
                    12: 31}

    if 1 <= month <= 12 and 1 <= day <= day_in_month[month]:
        return True
    return False

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
