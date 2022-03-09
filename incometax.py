AI = input("enter the your incomeo the year: ")
#this program calculate income tax
chunk = 500000
remember = AI % chunk
#calculate the ammount subject of the income tax
A = AI - remember
chunk_count = A / chunk
Taxable_chunk_count = chunk_count - 1
#def import operating system
I = 1
tax = 0
while I <= Taxable_chunk_count:
    tax = tax + chunk * 0.04 * I
    I = I + 1
    #return the calculate
    ex_tax= remember * 0.04 * chunk_count
    tot_tax = tax + ex_tax
    
    #print("the tot tax")
    print("your income tax  last of the tot_tax ")
  
   
    print("you must pay for the government ",tot_tax)

input("\n\n THANK YOU  \n\n PRESS ANY KEY TO EXIT THIS SOFTWARE...")    
   
   
  
