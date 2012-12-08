class code:
    name = "N/A"
    def __init__(self,inside,args = {}):
        self.inside = inside
        self.args = args
    def code(self):
        s= ""
        for i in self.args:
            s += i+"="self.args[i]
            
        return = "<"+self.name+s+">"+self.inside+"<"+self.name+">"
class html(code):
    name = "html"
    def __init__(self,inside,args={}):
        super.__init__(inside,args)
class head(code):
    name = "head"
    def __init__(self,inside):
        super.__init__(inside,args={})
class body(code):
    name = "body"
    def __init__(self,inside):
        super.__init__(inside)
class title(code):
    name = "title"
    def __init__(self,title):
        super.__init__(inside=title,args={})
class link(code):
    name = "a"
    def __init__(self,name,url):
        super.__init__(inside=name,args={'href':url})
class para(code):
    name = "p"
    def __init__(self,text):
        super.__init__(inside=text)
