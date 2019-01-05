#Question 1 : Degree Centigrade to Fahrenheit :-

c = (float(input("Please enter the temperature in Degree Centigrade to convert to Fahrenheit \nCentigrade: ")))
f = ((c*1.8)+32)
print("\nFahrenheit :", str(f))




#Question 2 : Degree Fahrenheit to Centigrade :-

f = (float(input("Please enter the temperature in Degree Fahrenheit to convert to Centigrade \nFahrenheit: ")))
c = ((f-32)/1.8)
print("\nCentigrade :", str(c))


#Question 3 : Area of Triangle :-

b = (float(input("Please enter the following values to calculate Area Of Triangle \nBase  : ")))
h = (float(input("Height: ")))
a = ((b*h)/2)
print("\nThe Area of the Triangle is : ", str(a))



#Question 4 : Volume Of Sphere :-

from math import pi
r = (float(input("Please enter the value of Radius to calculate the Volume of the sphere \nRadius: ")))
v = ((4/3)*pi*(r**3))
print("\nVolume of Sphere: ", str(v))


#Question 5 : Upper, Lower and Title case :-

name = input("Please enter your Full Name : ")
print("\nUpper Case: ", name.upper())
print("Lower Case: ", name.lower())
print("Title Case: ", name.title())
