max_marks=["05","05","05","07","05","10","08","15"]
needed_length=16

quit=True
while quit:
    entered_marks=input('\nEnter the marks - ')
    formed_marks=[]
    index=0
    validity=1
    if entered_marks=="q":
        quit=False

    elif needed_length!=len(entered_marks):
        print("Invalid input ")
    
    
        
    else:    
        for max_mark in max_marks:
        
    
            count=len(str(max_mark))+index
        
            formed_marks.append(entered_marks[index:count])
            index=count
    

        total=0
        x=0
        for mark in formed_marks:
            if int(mark)>int(max_marks[x]):
                print("\ninvalid marks for question ", x+1)
                print("mark should be below",int(max_marks[x])+1 ,"\nBut the given mark is",mark)
                validity=0
            else:
                total=total+int(mark)
                validity=1
            x=x+1
        if validity==1:

            print("\nTotal= ",total)
        print("\n..............................................................................")
else:
    print("program closed\n\nThank you for using !")