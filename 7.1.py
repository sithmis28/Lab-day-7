count=0
total=0
while count<=5:
  unit=float(input("enter units"))
  if unit<=100:
     bill=unit*10
  else:
      if unit<=200:
          bill=(100*10)+((unit-100)*15)
      else:
        bill=(100*10)+(100*15)+((unit-200)*20)
  count=count+1
  print("bill amount is Rs:",bill)
 
    


