weight=int(input("weight :"))
op=input("(k)g or (l)bs :")
if op.upper() == "K":
    converted=weight/0.45
    print("Weight in Lbs: "+str(converted))
else:
    converted=weight*0.45
    print("weight in Kgs :"+ str(converted))
