n=str(input("Enter the student type"))
if  n=="MSDS":
      x=float(input("Enter tution fees "))
      y=float(input("Enter bus fees"))
      n=x+y;
      print("the fees to be paid by the student is Rs.",n)
elif  n=="MSH":
      x=float(input("Enter tution fees "))
      z=float(input("Enter hostel fees"))
      n=x+z;
      print("the fees to be paid by the student is Rs.",n)
elif  n=="MGDS":
       x=float(input("Enter tution fees "))
       y=float(input("Enter bus fees"))
       n=x*150/100+y;
       print("the fees to be paid by the student is Rs.",n)
elif n=="MGSH":
      x=float(input("Enter tution fees "))
      z=float(input("Enter hostel fees"))
      n=x*150/100+z;
      print("the fees to be paid by the student is Rs.",n)
        
