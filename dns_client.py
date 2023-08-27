from dns_server import *

class webPC:
    def getIP(url):
        ip = DNS_Server.returnIP(url)
        if ip == None:
            return "Website not found."
        else:
            return "Connecting to " + ip
        
    def getURL(ip):
        url = DNS_Server.returnURL(ip)
        if url == None:
            return "URL not Found."
        else:
            return "Welcome to " + url

if __name__ == "__main__":
    a = webPC.getIP("www.cisco.com")
    print(a)
    b = webPC.getURL("1.1.1.1")
    print(b)
            
        
        