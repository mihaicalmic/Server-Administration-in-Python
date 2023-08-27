class SingleServer:
    __ipAddress = "192.168.1.1"
    __instance = None
    __startIP =2
    __endIP = 254
    
    def __init__(self,name):
        if SingleServer.__instance != None:
            print("Already in use")  
        else:
            self.name = name
            SingleServer.__instance = self
            
            
    def getInstance(self):
        if SingleServer.__instance == None:
            SingleServer("default")
        return SingleServer.__instance
    
    @staticmethod
    def DHCPconfig(startIP,endIP):
        SingleServer.__startIP = startIP
        SingleServer.__endIP = endIP
        
    @staticmethod    
    def DHCPrequest():
        if SingleServer.__startIP < SingleServer.__endIP:
            ip = "192.168.1." +str(SingleServer.__startIP)
            SingleServer.__startIP +=1
            return ip
        else:
           print("no more IPs")
           
    @staticmethod   
    def returnIP():
        return SingleServer.__ipAddress
        
if __name__ == "__main__":    
    a = SingleServer("d")
    a = a.DHCPrequest()
    print(a)
    b = SingleServer("s")
    b = b.DHCPrequest()
    print(b)
    c = SingleServer.returnIP()
    print(c)
    
    
        
            
    
    