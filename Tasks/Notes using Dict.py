class Notes:
    def __init__(self):
        self.Notes = {}
        
    def addtitle(self,title, content):
        self.Notes[title] = self.Notes.get(title, content)
        
    def process(self):
      while True:
        n = int(input("enter the number 1  for writting content and 2 for retriving the  data"))
        if n == 1:
            self.addtitle(raw_input("enter the title :"),raw_input("enter the content:"))
            
        elif n==2:
          if self.Notes == {}:
              self.addtitle(raw_input("enter the title :"),raw_input("enter the content:"))
              #print (self.Notes)it prints the dictionay
          else:
              
            for a in enumerate(self.Notes,1): #it  get the index for  keys-valuespairs
                print (a)
                
            self.Notes.items()
            d = [(k, v) for k, v in self.Notes.items()]  # converts into list
            i=int(input("enter the number for retriving the data"))
            print (d[i-1])

o = Notes()
o.process()
