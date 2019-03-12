import math
#Program to find the Sum, Mean, and Standard Deviation
#Version 1- Find the above with hard coded values and print results. Commented out for final Version
""" num1 = 5.0
num2 = 65.0
num3 = 2.0
num4 = 10.0
num5 = 7.0
#Sum
sum = num1 + num2 + num3 + num4 + num5
print(str(sum)) #python requires you to str() to visualize numbers
#Mean
mean = sum / 5
print(str(mean))
#Standard Deviation
Deviationnum1 = num1 - mean
Deviationnum2 = num2 - mean
Deviationnum3 = num3 - mean
Deviationnum4 = num4 - mean
Deviationnum5 = num5 - mean
std = math.sqrt(((Deviationnum1 ** 2) + (Deviationnum2 ** 2) + (Deviationnum3 ** 2) + (Deviationnum3 ** 2) + (Deviationnum4 ** 2)+ (Deviationnum5 ** 2)) / 5)
print(str(std))
"""

#Version 2: Allow User inputs
# the method 'input()' from the improt 'sys' assigns the input data to a variable
print("Enter five numbers to find their Sum, Mean, and Standard Divation")
a, b, c, d, e = map(float, raw_input("Numbers: ").split())
sum = a + b + c + d + e
print("Sum: " + str(sum))
mean = sum / 5
print("Mean: " + str(mean))
dA = (a - mean)
dB = (b - mean)
dC = (c - mean)
dD = (d - mean)
dE = (e - mean)
std = math.sqrt(((dA ** 2) + (dB ** 2) + (dC ** 2) + (dD ** 2) + (dE ** 2)) / 5)
print("Standard Deviation: " + str(std))
input("End? : ")
