class DNS_Server:
    
    dns_file = "data.txt"
    
    @staticmethod
    def read_dns():
        dns = {}
        with open(DNS_Server.dns_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().split(",")
                dns[line[0]] = line[1]
        return dns

    @staticmethod
    def write_dns(dns):
        with open(DNS_Server.dns_file, 'w') as f:
            for ip, url in dns.items():
                f.write(ip + "," + url + "\n")

    @staticmethod
    def returnIP(url):
        dns = DNS_Server.read_dns()
        for key, value in dns.items():
            if url == value:
                return key
        #else:
        #    print("IP not found.")
            
    @staticmethod
    def returnURL(ip):
        dns = DNS_Server.read_dns()
        if ip in dns:
            return dns[ip]
        else:
            return "URL not found."

    @staticmethod
    def addDNS(ip, url):
        dns = DNS_Server.read_dns()
        dns[ip] = url
        DNS_Server.write_dns(dns)
        return "Website added"
        
    @staticmethod
    def removeDNS(ip):
        dns = DNS_Server.read_dns()
        if ip in dns:
            del dns[ip]
            DNS_Server.write_dns(dns)
            print("Website removed.")
        else:
            print("IP not found.")
            
    @staticmethod
    def listDNS():
        dns = DNS_Server.read_dns()
        for key, value in dns.items():
            print(key, "\t" , value)
            
    #@staticmethod
    #def returndns():
    #    dns = DNS_Server.read_dns()
    #    return dns
    
if __name__ == "__main__":
    #ip = input("Enter an IP you want to add to the DNS server: ")
    #url = input("Enter the URL asociated with this IP address: ")
    #DNS_Server.addDNS(ip,url)
    
    #DNS_Server.addDNS("1.1.1.1","www.mihail.com")
    #ip = DNS_Server.returnIP("www.google.com")
    #print(ip)
    #ip = DNS_Server.returnIP("www.pepe.com")
    #print(ip+"gangster")
    #url = DNS_Server.returnURL("192.168.10.1")
    #print(url)
    #DNS_Server.removeDNS("192.188.23.54")
    #ip = DNS_Server.returnIP("www.youtube.com")
    #print(ip)
    #url = DNS_Server.returnURL("1.1.1.1")
    #print(url)
    #DNS_Server.removeDNS("1.1.1.1")
    DNS_Server.listDNS()
    
    
    

