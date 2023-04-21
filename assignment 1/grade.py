a=input("name khod ra vared konid:")
b=input("name khanevadegie khod ra vared konid:")
c=float(input("nomre darse avale shoma:"))
d=float(input("nomre darse dovom shoma:"))
e=float(input("nomre darse sevom shoma:"))
grade= (c+d+e)/3
print(a,b,"moadel shoma:",grade)
if grade>=17:
    print("great",a,b)
elif grade<17 and grade>=12:
    print("normal",a,b)
elif grade<12:
    print("fail",a,b)