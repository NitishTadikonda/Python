class Notes:
    def __init__(self):
        self.title = []
        self.content = []
        
    def process(self):
        while True:
            n = int(input("enter the number 1  for writting content and 2 for retriving the  data"))
            if n == 1:
                def addtitle(title,content):
                    self.title.append(title) 
                    self.content.append(content)
                addtitle(raw_input("enter title"),raw_input("enter content"))
            elif n==2:
                if self.title == [] or self.content == []:
                    def addtitle(title,content):
                        self.title.append(title) 
                        self.content.append(content)
                    addtitle(raw_input("enter title"),raw_input("enter content"))
                    
                else:
                    c = enumerate(self.title,1)
                    for i in c:
                        print(i)
                    i=int(input("enter the number for retriving the data"))
                    #d = map(lambda x,y:(x,y),self.title,self.content)to display in list like as zip function
                    print("Title:%s\nContent:%s"%(self.title[i-1],self.content[i-1]))


o = Notes()
o.process()
