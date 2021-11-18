num=int(input("enter the number is"))
temp=num
reversed=0
while num!=0:
	digit=num%10
	reversed=reversed*10+digit
	num//=10
print("reversed number:"+str(reversed))
print("the number is",temp)
if(reversed==temp):
	print("the number is a palidrome number")
else:
	print("the number is not a palidrome number")	