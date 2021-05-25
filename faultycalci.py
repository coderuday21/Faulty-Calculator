faulty={"45*3":555,"56+9":77,"56/6":4}
opr=input("+,-,/,* ")
var1=input()
var2=input()
equ=var1+opr+var2
if equ in faulty:
    print(faulty[equ])
else:
    print(eval(equ))
