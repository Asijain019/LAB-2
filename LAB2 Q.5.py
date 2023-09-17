#Find the area of a Circle of radius r. Only radius between 1 and 100 should be accepted.
r=float(input("enter the value:"))
area=3.14*r**2
if 1<r<=100 :
    print("the area of the circle is:",area)
else:
    print("not accepted")


