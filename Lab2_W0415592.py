""" /**************************************************
Lab#2
Title: Hello world and basic numerical formats
Student: Joshua Z. Tynes
Student #: W0415592
Instructor: Ricardo Bautista Quintero
Date:January 18th 2021
NSCC Ivany Campus
/**************************************************"""
"""

We will demonstrate the following topics:

1.) Print Text to Serial Monitor
2.) Types of Numbers in Python
2.) Basic Arithmetic
3.) Differences between classic division and floor division
4.) Object Assignment in Python

"""
def program_1():
   
    #Hello World
    print("Hello World")
    s = 'Hello World'
   
    print(s)
    print(s.upper())
    print(s.lower())
    print()
    
    #NUMBERS
    a = 2
    b = 3
    f = 2e4
    print(a)
    print("is an integer")
    print(f)
    print("is an floating point number")
    print("a is : ", a)
    print("b is : ", b)
    print("a + b is :", a+b)
    print("a - b is :", a-b)
    print("a * b is :", a*b)
    print("a / b is :", a/b)
    print("a divided by b using floor division is :", a//b)
    print("10 divided by 3 using floor division is :", 10//3)
    
if __name__ == '__main__':
    program_1()