Number = str(input("Enter your number to find lucky number:"))
total = 0
n =0

for i in Number:
    total = total + int(i)

#print(total) 

if len(str(total)) >= 2:
    for count in  str(total) :
        n = n + int(count)
        print "\nThe lucky nmuber is:",n
        break
else:
    print "\nThe lucky number is:",total
