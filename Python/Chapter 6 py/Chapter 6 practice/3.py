p1="Make a lot of money"
p2="Buy now"
p3="Subscribe this"
p4="Click here"
message=input()
if((p1 in message) or (p2 in message)or(p3 in message)or(p4 in message)):
    print("Its a spam")
else:
    print("Not spam")