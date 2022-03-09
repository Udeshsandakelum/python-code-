input1 = int(input("Enter the number of blocks:"))

class Main():
    def __init__(self, input2,var1,var2,num_blocks,height):
        self.input2 = input2
        self.var1 = var1
        self.var2 = var2
        self.num_blocks = num_blocks
        self.height = height
        for i in range(1,self.input2):
            self.var1 = self.var1 + 1
            self.num_blocks = self.num_blocks + self.var1
            self.var2 = self.var2 + 1
            if self.num_blocks > self.input2:
                break
            if self.var2 == self.var1:
                self.height = self.height + 1
        print(self.height)
object = Main(input1,0,0,0,0)                
        
                


        
