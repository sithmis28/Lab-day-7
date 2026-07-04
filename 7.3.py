bill=0
count=0
price=float(input("enter item price"))
while price !=0:
    bill=bill+price
    count=count+1
    price=float(input("enter item price (or 0 to stop):"))
if count>0:
    avg_price=bill/count
else:
    avg_price=0
print("total bill is",bill)
print("number of item purchased:",count)
print("avg price is",avg_price)
