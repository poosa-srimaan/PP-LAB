def deposit(balance,money):
	return balance+money

def withdraw(balance,money):
	return balance-money

def print_balance(bal):
    print("\nYOUR CURRENT BALANCE = ",bal)

def last_5(li,acc_num,acc_name,acc_IFSE):
	if len(li)>=5:
		print("\t\tLAST FIVE TRANSACTIONS\n")
		print("ACCOUNT NUMBER = ",acc_num,"               ACCOUNT IFSE CODE = ",acc_IFSE)
		print("ACCOUNT NAME   = ",acc_name)
		print("DEPOSIT         WITHDRAW         TOTAL_BALANCE")
		for i in range(len(li)-5,len(li)):
			for j in range(3):
				a=len(str(li[i][j]))
				print(li[i][j],end=' ')
				for k in range(18-a):
					print("",end=' ')
			print()
	else:
		print("\t\tLAST FIVE TRANSACTIONS")
		print("ACCOUNT NUMBER = ",acc_num,"               ACCOUNT IFSE CODE = ",acc_IFSE)
		print("ACCOUNT NAME   = ",acc_name)
		print("DEPOSIT         WITHDRAW         TOTAL_BALANCE")
		for i in range(len(li)):
			for j in range(3):
				a=len(str(li[i][j]))
				print(li[i][j],end=' ')
				for k in range(18-a):
					print("",end=' ')
			print()
	print_balance(li[i][j])
	print("\n")

acc_num=int(input("Enter your account number: "))
acc_name=input("Enter your name: ")
acc_IFSE=input("Enter your IFSE code: ")
acc_bal=0
li=[]
while(True):
	sub_li=[]
	print("Enter (1) to Deposit\nEnter (2) to Withdraw\nEnter (3) to Check Balance\nEnter (4) to check last five transaction\nEnter (5) to change your NAME\nEnter (6) to EXIt")
	n=int(input("Choose the number: "))

	if n==1:
		dep=int(input("Enter Amount to Deposit: "))
		acc_bal=deposit(acc_bal,dep)
		sub_li=[dep,0,acc_bal]
		li.append(sub_li)
		print(dep,",AMOUNT DEPOSIT SUCCESSFULLY")
		print("\n")
	elif n == 2:
		wit=int(input("Enter Amount to withdraw: "))
		acc_bal=withdraw(acc_bal,wit)
		sub_li=[0,wit,acc_bal]
		li.append(sub_li)
		print(wit,",AMOUNT WITHDRAW SUCCESSFULLY")
		print("\n")

	elif n == 3:
		print("ACCOUNT_NUMBER = ",acc_num,"                ACCOUNT_IFSE_CODE = ",acc_IFSE)
		print("ACCOUNT_NAME   = ",acc_name)
		print("\nACCOUNT BALANCE = ",acc_bal)

	elif n == 4:
		last_5(li,acc_num,acc_name,acc_IFSE)

	elif n == 5:
		acc_name=input("please enter your new name: ")

	elif n==6:
		break
	else:
		print("please choose  correct option")
