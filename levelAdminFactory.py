from singleServer import SingleServer
from NetworksFactory import NetworkFactory, CiscoSwitch, Repeater, SecurityHUB
from dns_server import DNS_Server
from Authentication import User
from client_socket import Client
from email_receiver import Receiver
from email_sender import Sender

class L15Access:
    def __init__(self,name):
        self.name = name
        self.level = 15
        
    def dhcpConfig(self,startIP,endIP):
        SingleServer.DHCPconfig(startIP,endIP)
    
    def dhcpRequest(self):
        a = SingleServer.DHCPrequest()
        print(a)
        
    def dhcp_ip(self):
         a = SingleServer.returnIP()
         print("The DHCP server ip address is",a)
        
    
    def powerOn(self,choice):
        device = NetworkFactory.networkstatus(choice)
        device.powerUP()
        
    def powerOff(self,choice):
        device = NetworkFactory.networkstatus(choice)
        device.shutdown()
    def Configure(self,choice):
        device = NetworkFactory.networkstatus(choice)
        device.configure()
        
    def listDNS(self):
        DNS_Server.listDNS()
        
    def addDNS(self,ip,url):
        DNS_Server.addDNS(ip,url)
    
    def removeDNS(self,ip):
        DNS_Server.removeDNS(ip)
    
    def listUsers(self):
        User.list_user()
        
    def addUser(self,list1,name):
        User.addUser(list1,name)
        
    def removeUser(self,list1,name):
        User.removeUser(list1,name)
        
    def readRequests(self):
        data = Receiver.get_inbox()
        return data
        
        
class L1Access:
    def __init__(self,name):
        self.name = name
        self.level = 1
        
    def dhcpRequest(self):
        a = SingleServer.DHCPrequest()
        print(a)
    
    def powerOn(self,choice):
        device = NetworkFactory.networkstatus(choice)
        device.powerUP()
        
    def powerOff(self,choice):
        device = NetworkFactory.networkstatus(choice)
        device.shutdown()
    
    def getURL(self,ip):
       Client.dnsrequest(ip)
       
    def getIP(self,url):
       Client.dnsrequest(url)
    
    def listUsers(self):
        User.list_user()
        
    def sendRequests(self,message):
        Sender.send_email(message)
 

class L0Access:
    def __init__(self,name):
        self.name = name
        self.level = 0
        
    def powerOn(self,choice):
        device = NetworkFactory.networkstatus(choice)
        device.powerUP()
        
    def powerOff(self,choice):
        device = NetworkFactory.networkstatus(choice)
        device.shutdown()
    
    def getIP(self,url):
       Client.dnsrequest(url)
       
    def sendRequests(self,message):
        Sender.send_email(message)
        
        
        
class AdminFactory:
    @staticmethod
    def buildAdmin(priority):
        if priority == 0:
            return L0Access("default")
        if priority == 1:
            return L1Access("default")
        if priority == 15:
            return L15Access("default")
        else:
            print("invalid priority")
            
#Just some function being run to test functionality faster then accessing UserIntercation class.
if __name__ == "__main__":
    #admin = AdminFactory.buildAdmin(1)
    #admin.getURL("126.56.97.12")
    #admin.getIP("www.google.com")
    #admin2 = AdminFactory.buildAdmin(0)
    #admin2.getIP("www.google.com")
    admin = AdminFactory.buildAdmin(15)
    admin.addUser("admins","Mihail")
    admin.listUsers()
    
    #admin.listDNS()
    #admin.addDNS("1.1.1.2","www.test.com")
    #admin.listDNS()
    #print()
    
    #admin.dhcpRequest()
    #user = AdminFactory.buildAdmin(0)
    #user.getIP("www.test.com")
    user = AdminFactory.buildAdmin(1)
    user.sendRequests("Add a new user Chan")
    data = admin.readRequests()
    for email in data:
        print("Email request number",email['request_num'])
        print(email['date'])
        print(email['body'])

    

    
    
