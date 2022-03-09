User_input = int(input("Enter the number:"))
for i in  range(1,User_input):
    count = 0
    for x in range(1,i+1):
        if (i%x == 0):
            count += 1
    if (count == 2):
        print(i)



        
