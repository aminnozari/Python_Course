import math
print("adad haye morede nazar khod ra vared konid")
a=int(input("1:"))
b=int(input("2:"))
print("""
      chose your action:
      1=+
      2=-
      3=/
      4=*
      5=radical
      6=sin
      7=cos
      8=tan
      9=cot
      10=factorial
      """)
p=int(input())
if p==1:
    r=a+b
elif p==2:
    if a>b:
        r= a-b
    else:
        r= b-a
elif p==3:
    if b==0:
        print("error")
    else:    
        r= a/b
elif p==4:
    r=a*b
elif p==5:
    print("radical adad aval:")
    r=math.sqrt(a)
elif p==6:
    print("sin adad aval:")
    pi= math.pi/180
    a= a*pi
    r=math.sin(a)
elif p==7:
    print("cos adad aval:")
    pi= math.pi/180
    a= a*pi
    r=math.cos(a)
elif p==8:
    print("tan adad aval:")
    pi= math.pi/180
    a= a*pi
    r= math.tan(a)
elif p==9:
    print("cot adad aval:")
    pi= math.pi/180
    a= a*pi
    r= 1/math.tan(a)
elif p==10:
    print("fact adad aval:")
    r= math.factorial(a)
print(r)