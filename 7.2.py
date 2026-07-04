count=0
eligible_count=0
not_eligible_count=0
total_attendance=0
while count<10:
    attendance=int(input("enter your attendance"))
    
    if attendance>=75:
        eligible_count=eligible_count+1
    else:
        not_eligible_count=not_eligible_count+1
    total_attendance=total_attendance+attendance
    count=count+1
avarage_attendance=total_attendance/10
print("eligible students",eligible_count)
print("not eligible students",not_eligible_count)
print("avg studence",avarage_attendance)
    
