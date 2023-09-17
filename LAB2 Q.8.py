#take a value of year as input and find whether it is a leap year or not. Consider all the cases of valid and invalid inputs. Write down the test cases for the same.
year=int(input("enter the value:"))
if year%4==0:
    print("its a leap year")
else:
    print("its not a leap year")
    