def add_Number( num1, num2):
	return num1+num2
def multi_Number( num1, num2):
	return num1*num2
	
def sub_Number( num1, num2):
	return num1-num2
	
def Div_Number( num1, num2):
	return num1/num2
	
def main():
	x=input("Type C to exit..  ")
	if (x=='C' or x=='c'):
			exit()
	print("choose the operation..form the list below.." )
	operation=input("chose '*','+','/','-'")
	if (operation!='+' and operation!='-' and operation!='*' and operation!='/'):
		print("Please choose valid a operation..")
		return(main())
		
	else:
		val1=float(input("enter the first number : "))
		val2=float(input("enter the second number: "))
		if(operation=='+'):
			print(add_Number(val1,val2))
			return(main())
			
		elif(operation=='-'):
			print(sub_Number(val1,val2))
			return(main())	
			
		elif(operation=='*'):
			print(multi_Number(val1,val2))
			return(main())
			
		else:	
			print(Div_Number(val1,val2))
			return(main())
main()
