#Q1 What is Time Tuple?

Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −

Index	Field	Values
0	4-digit year	2008
1	Month	1 to 12
2	Day	1 to 31
3	Hour	0 to 23
4	Minute	0 to 59
5	Second	0 to 61 (60 or 61 are leap-seconds)
6	Day of Week	0 to 6 (0 is Monday)
7	Day of year	1 to 366 (Julian day)
8	Daylight savings	-1, 0, 1, -1 means library determines DST

The above tuple is equivalent to struct_time structure. This structure has following attributes −

Index	Attributes	Values
0	tm_year	2008
1	tm_mon	1 to 12
2	tm_mday	1 to 31
3	tm_hour	0 to 23
4	tm_min	0 to 59
5	tm_sec	0 to 61 (60 or 61 are leap-seconds)
6	tm_wday	0 to 6 (0 is Monday)
7	tm_yday	1 to 366 (Julian day)
8	tm_isdst	-1, 0, 1, -1 means library determines DST


#Q2 Write a program to get formatted time.

# import time

print(time.ctime())
print("\n")


#Q3 Extract month from the time.

import time
print(time.ctime())
print("\n")
s = (time.gmtime())
print("the month from the time  :",s)
print("the month is :",s[1])

#Q4 Extract day from the time.
 
import time
t = time.gmtime()
print("the current time is :",time.ctime())
day = t[6]
if day == 0:
	print("monday")
if day == 1:
	print("tueday")
if day == 2:
	print("wednesday")
if day == 3:
	print("thrday")
if day == 4:
	print("friday")
if day == 5:
	print("satday")
if day == 6:
	print("sunday")
	




#Q5 Extract date (ex : 11 in 11/01/2021) from the time.

import time
t=time.gmtime()
date=t[2]
print("the current date is: ",date)
 

#Q6 Write a program to print time using localtime method.
 
import time
print(time.localtime())

#Q7 Find the factorial of a number input by user using math package functions.

import math
x = math.factorial(int(input("Enter the number you want to find the factprial: ")))
print("factorial : ",x)
print("\n")

#Q8 Find the GCD of a number input by user using math package functionsfactor

import math
x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))
print("GCD is : ",math.gcd(x,y))
print("\n")

# Q9 Use OS package and do the following tasks: 
# 1 Get current working directory.
# 2 Get the user environment.

import os
print("\n")
print(os.getcwd())
print("\n")
print(os.name)
print("\n")
print(os.listdir())
print("\n")
print(os.environ)




