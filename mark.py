eng=int(input("enter the eng value"))
tam=int(input("enter the tam value"))
mat=int(input("enter the mat value"))
sci=int(input("enter the sci value"))
soc=int(input("enter the soc value"))
print("the eng mark is",eng)
print("the tam mark is",tam)
print("the mat mark is",mat)
print("the sci mark is",sci)
print("the soc mark is",soc)
if('(m1>=35)' and '(m2>=35)' and '(m3>=35)' and '(m4>=35)' and '(m5>=35)'):
           print("pass")
else:
		   print("fail")
total=eng+tam+mat+sci+soc
average=total/5
print("the total mark is",total)
print("the average is",average)		   