marks1=int(input())
marks2=int(input())
marks3=int(input())
total_parcentage=(100*(marks1+marks2+marks3)/300)
if(total_parcentage>40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed ",total_parcentage)
else:
    print("Failed ",total_parcentage)