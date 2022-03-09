
#Get input from user
inp = int(input("Enter the number of blocks:"))
#Create class as new
class new():
    #Define a function using __init__ methode
    def __init__(self,inp,exvar,block,num,length_pyramid):
        self.inp = inp
        self.exvar = exvar
        self.block = block
        self.num = num 
        self.length_pyramid = length_pyramid
        #Looping using while loop and self parameter
        while self.exvar < self.inp:
            self.block = self.block + self.exvar
            if self.block <= self.inp:
                self.length_pyramid = self.length_pyramid + 1
            else:
                break
            self.num += 1
            self.exvar += 1
        print(self.length_pyramid - 1)    

#Create object to call the class
object = new(inp,0,0,1,0)
       

        
