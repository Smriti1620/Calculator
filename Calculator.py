print("CALCULATOR")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
print("choice:('1','2','3','4')")
total=0
while(True):
 choice=int(input("Enter a Choice"))
 A=int(input("Enter One number"))
 B=int(input("Enter Another number"))
 if choice==0:
    print("Exit")
    break
 elif choice==1:
    print(A,"+",B,"=",A+B)
 elif choice==2:
    print(A,"-",B,"=",A-B)
 elif choice==3:
    print(A,"*",B,"=",A*B)
 elif choice==4:
    print(A,"/",B,"=",A/B)
 else:
   print("READ INSTRUCTIONS CAREFULLY")