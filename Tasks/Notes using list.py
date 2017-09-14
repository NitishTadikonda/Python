class Notes:
    def __init__(self):
        self.title = []
        self.content = []
        
    def addtitle(self,title,content):
        self.title.append(title)
        self.content.append(content)
        
    def process(self):
        while True:
            n = int(input("Enter the number 1  for writting content and 2 for retriving the  data"))
            if n == 1:
                self.addtitle(input("Enter Title:"),input("Enter Content:"))
        
            elif n==2:
                if self.title == [] or self.content == []:
                    self.addtitle(input("Enter Title:"),input("Enter Content:"))                    
                else:
                    c = enumerate(self.title,1)
                    for i in c:
                        print(i)
                    i=int(input("Enter the number for retriving the data"))
                    #d = map(lambda x,y:(x,y),self.title,self.content)to display in list like as zip function
                    print("Title:%s\nContent:%s"%(self.title[i-1],self.content[i-1]))


o = Notes()
o.process()
