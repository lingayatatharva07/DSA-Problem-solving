salary=int(input('enter your salary:'))
rating=int(input('enter your performance appraisal rating:'))
increment=0
if rating>=1 and rating<=3:
    increment=salary*10/100
elif rating>=3.1 and rating<=4:
    increment=salary*30/100
elif rating>=4.1 and rating<=5:
    increment=salary*40/100
else:
    print('Invalid rating')
print('incremented salary:',increment+salary)    
#-------------------------------------------------------------------
# basicsalary=20000
# HRA=basicsalary*20/100
# TA=basicsalary*30/100
# DA=basicsalary*45/100
# GrossSalary=basicsalary+HRA+TA+DA
# print('GrossSalary:',GrossSalary)