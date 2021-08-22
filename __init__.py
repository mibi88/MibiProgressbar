# coding: utf-8

class progressbar():
    def __init__(self, title = "Progress", value = 0, width = 10, char = "█", uchar = "-", after = ""):
        try:
            self.title = str(title)
        except:
            raise ValueError("Bad title")
        try:
            self.valueint = int(value)
        except:
            raise ValueError("Bad value")
        try:
            self.widthint = int(width)
        except:
            raise ValueError("Bad width")
        self.unit = self.widthint / 100
        self.nvalue = self.unit * self.valueint
        #print(nvalue)
        try:
            self.charstr = str(char)
        except:
            raise ValueError("Bad char")
        try:
            self.ucharstr = str(uchar)
        except:
            raise ValueError("Bad uchar")
        try:
            self.after = str(after)
        except:
            raise ValueError("Bad after")
    def buildbar(self):
        self.pbartext = self.title + " ["
        for i in range(self.widthint):
            if i < self.nvalue:
                self.pbartext += self.charstr
            else:
                self.pbartext += self.ucharstr
        self.pbartext += "] " + self.after
    def getbar(self):
        return self.pbartext
    def displaybar(self):
        print(self.pbartext, end="\r")
    def updatebar(self, title = None, value = None, width = None, char = None, uchar = None, after = None):
        if title != None:
            try:
                self.title = str(title)
            except:
                raise ValueError("Bad title")
        if value != None:
            try:
                self.valueint = int(value)
            except:
                raise ValueError("Bad value")
        if width != None:
            try:
                self.widthint = int(width)
            except:
                raise ValueError("Bad width")
        self.unit = self.widthint / 100
        self.nvalue = self.unit * self.valueint
        if char != None:
            try:
                self.charstr = str(char)
            except:
                raise ValueError("Bad char")
        if uchar != None:
            try:
                self.ucharstr = str(uchar)
            except:
                raise ValueError("Bad uchar")
        if after != None:
            try:
                self.after = str(after)
            except:
                raise ValueError("Bad after")
