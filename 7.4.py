balance=50000
total=0
withdrawals=0
while:
    print("current balanca",balance)
    amount=float(input("enter withdrawal amount (or -1 to stop):"))
    if amount ==-1:
        break
    if amount>balance:
        print("insufficient balance")
    else:
        balance=balance-amount
        total=total+1
        withdrawals=withdrawal+1
        print("withdrawal successful")
        
