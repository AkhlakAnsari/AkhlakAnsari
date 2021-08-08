#area of triangle
#written by ER AKHLAK ANSARI
a= float(input("side1:"))
b=float(input("side2:"))
c=float(input("side3:"))
#perimeter=(a+b+c)
p=(a+b+c)
print("PERIMETER OF TRIANGLE=",p)
#SEMIPERIMETER OF TRIANGLE
s=(a+b+c)/2
print("SEMIPERIMETER OF TRIANGLE =",s)
#heron's formula of triangle

#x=sqrt(s*(s-a)*(s-b)*(s-c))
import math
area=math.sqrt((s*(s-a)*(s-b)*(s-c)))
#upto to decimal point result value
print(" AREA OF TRIANGLE  = %.2f " % area)
#akhlakansari94@gmail.com




