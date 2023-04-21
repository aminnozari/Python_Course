a=int(input("vazn khod ra bar hasb kilogram vared konid:"))
b=float(input("ghad khod ra bar hasb metr vared konid:"))
bmi= a/(b**2)
print("bmi shoma=",bmi)     
if bmi<=18.5:
    print("you are: underweight")
elif bmi>18.5 and bmi<=24.9:
    print("you are: normal")
elif bmi>25 and bmi<=29.9:
    print("you are: owerweight")
elif bmi>30 and bmi<=34.9:
    print("you are: obese")
elif bmi>=35:
    print("you are: extremely obese")
    