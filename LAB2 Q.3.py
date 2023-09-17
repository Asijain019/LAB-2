#Take 2 integers x and y as input and find whether y is divisible by x or not. For negative integers,display the message"invalid input".
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
if x<0 or y<0 :
    print("INVALID INPUT")
elif y%x==0 :
        print("YES DIVISIBLE")
else:
    print("NOT divisible")







