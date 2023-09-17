#Using the temperature conversion formula, calculate the value at which the Celsius and corresponding Fahrenheit values are the same.
print("enter the temperature in celsius:")
cel=float(input())
fah=(cel*1.8)+32
if cel==fah :
    print("the required tem at which the values are same is:",fah)
else:
    print('not same')
