import math as mt

print("use sqrt({NUMBER})")

def calc():
    try:
        
        x = input(">HERE< ")
        y = x.replace("^","**")
        y = y.replace("sqrt","mt.sqrt")
        z = eval(y)
        print(z)
        calc()
        
    except:
        
        print("invalid")
        calc()
        
calc()