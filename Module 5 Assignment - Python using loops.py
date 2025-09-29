#start#
##declare vars##
numList=[]
number=0
counter=0
i=0
##get user input to make list##
while counter < 15:
    number=input("Input a whole number: ")
    numList.append(int(number))
    counter=counter+1
##run the even/odd checker##
while i < counter:
    if numList[i]%2==0:
        print(str(numList[i]) + " is even.")
    else:
            print(str(numList[i]) + " is odd.")
    i=i+1
print("End program.")
#end#