from Authentication import User
from levelAdminFactory import AdminFactory


# Function creates returns users, Then they get saved loccaly to use.
user1 = User.return_users()
admins = user1[0]
normalUsers = user1[1]
beginners = user1[2]

#Create User Intiroduction and give Options
while True:
    print ("Welcome to the network admin application")
    print ("What tasks do you need performed?")
    print("")
    print("Press 1 for DHCP Configuration")
    print("Press 2 for Accessing Network Devices")
    print("Press 3 for User Management")
    print("Press 4 for DNS Configurations")
    print("Press 5 for System Admin Requests")
    print("Press 0 to exit")
    print("")
    
    #Prompt the user for choice of task
    choice = input("What task do you want to perform?: ")
        # If the user chooses DHCP, prompt user for their priority
    if choice == '0':
        print("Goodbye")
        break
    elif choice == '1':
        #Prompt user for name, depending on what list they are in, create a respective admin class
        name = input("Enter your name: ")
        if name in admins:
            admin = AdminFactory.buildAdmin(15)
            print("You have the correct priority level for all DHCP Configurations ")
            print()
            while True:
                task = input("Press d to display the DHCP Server IP address \nPress c for DHCP Pool Configuration \nPress r for Request DHCP address \nPress 0 for exit  ")
                  
                if task == "r":
                    admin.dhcpRequest()
                    print()
                    
                elif task == "d":
                    admin.dhcp_ip()
                    print()
                
                elif task == "c":
                    startIP = (int(input("Enter start IP for DHCP Pool: ")))
                    endIP = (int(input("Enter end IP for DHCP Pool: ")))
                    admin.dhcpConfig(startIP,endIP)
                    print()
                
                elif task == "0":
                    break
                else:
                    pass
                
                
        elif name in normalUsers:
            admin = AdminFactory.buildAdmin(1)
            print("You have the priority level to perform the following actions ")
            while True:
                task = input("Press r for Request DHCP address \nPress 0 for exit:  ")
                if task == "r":
                    admin.dhcpRequest()
                    print()
                elif task == "0":
                    break
                else:
                    pass
                
            
        else:
            print("You dont have access to these configurations")
            print("")
            
            
    elif choice == '2':
        name = input("Enter your name: ")
        if name in admins:
            admin = AdminFactory.buildAdmin(15)
            print("You have the have access to all the devices.")
            while True:
                print()
                device = input("Press c for Cisco Switch \nPress s for Security Hub \nPress 0 for exit  ")
                      
                if device == "c":
                    print("Welcome to the Cisco Router")
                    task = input("Press u to power ON.\nPress d to shutdown. \nPress c to configure.\nPress 0 for exit  ")
                    if task == "u":
                        admin.powerOn("ciscoswitch")
                    elif task == "d":
                        admin.powerOff("ciscoswitch")
                    elif task == "c":
                        admin.Configure("ciscoswitch")
                    elif task == "0":
                        break
                    else:
                        pass
                elif device == "s":
                    print("Welcome to the Security Hub")
                    task = input("Press u to power ON.\nPress d to shutdown. \nPress 0 for exit  ")
                    if task == "u":
                        admin.powerOn("securityhub")
                    elif task == "d":
                        admin.powerOff("securityhub")
                    elif task == "0":
                        break
                    else:
                        pass
                    
                #this break allows return to the main menu
                elif device == "0":
                    break
                else:
                    pass
                
        if name in normalUsers:
            admin = AdminFactory.buildAdmin(1)
            print()
            print("You have the priority level to perform the following actions ")
            while True:
                print()
                device = input("Press c for Cisco Switch \nPress r for Repeater \nPress 0 for exit  ")
                      
                if device == "c":
                    print("Welcome to the Cisco Router")
                    task = input("Press u to power ON.\nPress d to shutdown. \nPress 0 for exit  ")
                    if task == "u":
                        admin.powerOn("ciscoswitch")
                    elif task == "d":
                        admin.powerOff("ciscoswitch")
                    elif task == "0":
                        break
                    else:
                        pass
                    
                elif device == "r":
                    print("Welcome to the Repeater")
                    task = input("Press u to power ON.\nPress d to shutdown. \nPress 0 for exit  ")
                    if task == "u":
                        admin.powerOn("repeater")
                    elif task == "d":
                        admin.powerOff("repeater")
                    elif task == "0":
                        break
                    else:
                        pass
                elif device == "0":
                    break
                else:
                    pass
        
        if name in beginners:
            admin = AdminFactory.buildAdmin(0)
            while True:
                print()
                print("You have the priority level to perform the following actions ")
                task = input("Press u to power on the Repeater.\nPress d to power off the Repeater. \nPress 0 for exit  ")
                if task == "u":
                    admin.powerOn("repeater")
                elif task == "d":
                    admin.powerOff("repeater")
                elif task == "0":
                    break
                else:
                    pass
        else:
            print("Sorry no access for you.")
            
    elif choice == '3':
        name = input("Enter your name: ")
        if name in admins:
            admin = AdminFactory.buildAdmin(15)
            print("You have access to add and remove users.")
            while True:
                print()
                task = input("Press l to list users\nPress a to add a user\nPress d to delete a user\nPress 0 for exit  ")
                if task == "l":
                    print()
                    admin.listUsers()
                elif task == "a":
                    list1 = input("Please enter a list to add the username to: ")
                    name1 = input("Please enter a name: ")
                    admin.addUser(list1,name1)
                    
                elif task == "d":
                    list1 = input("Please enter a list to remove the username from: ")
                    name1 = input("Please enter a name: ")
                    admin.removeUser(list1,name1)
                elif task == "0":
                    break
                else:
                    pass
        if name in normalUsers:
            admin = AdminFactory.buildAdmin(1)
            print()
            print("You have the priority level to view users.")
            while True:
                print()
                device = input("Press l list the users \nPress 0 for exit  ")
                      
                if device == "l":
                    print()
                    admin.listUsers()
                elif task == "0":
                    break
                else:
                    pass
        else:
            print("Sorry, no accces for you")
            print()
                    
                
    elif choice == '4':
        name = input("Enter your name: ")
        if name in admins:
            admin = AdminFactory.buildAdmin(15)
            print("You have access to configure the DNS Server.")
            while True:
                print()
                task = input("Press l to list the curent data\nPress a to add\nPress r to remove \nPress 0 for exit  ")
                
                if task == "l":
                    print("DNS Available Information")
                    admin.listDNS()
                
                elif task == "a":
                    print("Ready to add a new DNS address ?")
                    ip = input("Enter the Ip address you want to add: ")
                    url = input("Enter the associated url: ")
                    admin.addDNS(ip,url)
                elif task == "r":
                    print("Ready to delete a new DNS address ?")
                    ip = input("Enter the Ip address you want to remove: ")
                    admin.removeDNS(ip)
                    
                elif task == "0":
                    break
                else:
                    pass
        if name in normalUsers:
            admin = AdminFactory.buildAdmin(1)
            print("You have access to request IP and URL.")
            while True:
                print()
                task = input("Press i to access an IP\nPress u to access an URL\nPress 0 for exit  ")
                
                if task == "i":
                    print("Welcome to Chrome")
                    ip = input("Enter the Ip address you want to access: ")
                    admin.getURL(ip)
                
                elif task == "u":
                    print("Welcome to Chrome")
                    url = input("Enter the URL for your website: ")
                    admin.getIP(url)
                    
                elif task == "0":
                    break
                else:
                    pass
                
        if name in beginners:
            admin = AdminFactory.buildAdmin(0)
            print("You have access to internet.")
            while True:
                print()
                task = input("Press u to access an URL\nPress 0 for exit  ")
                
                if task == "u":
                    print("Welcome to Chrome")
                    url = input("Enter the URL for your website: ")
                    admin.getIP(url)
                    
                elif task == "0":
                    break
                else:
                    pass
                
    elif choice == '5':
        name = input("Enter your name: ")
        if name in admins:
            admin = AdminFactory.buildAdmin(15)
            print("You have access to the requests made by other users.")
            while True:
                print()
                task = input("Press r to read the latest requests. \nPress 0 for exit  ")
                if task == "r":
                    data = admin.readRequests()
                    #If no new emails, then reuturn a message
                    if data == []:
                        print("No new requests.")
                    #If new email are found, for each email returned, print the number of the email, the data and the request from the body.
                    for email in data:
                        print("Email request number",email['request_num'])
                        print(email['date'])
                        print(email['body'])
                        
                elif task == "0":
                    break
                else:
                    print("Invalid input")
                    
        if name in normalUsers:
            admin = AdminFactory.buildAdmin(1)
            print("You have access to request changes to the system.")
            while True:
                print()
                task = input("Press s to send a request to the admin.\nPress 0 for exit  ")
                
                if task == "s":
                    request1 = input("What system change do you require: ")
                    message = (name + " request.\n" + request1)
                    admin.sendRequests(str(message))
                    print("Request sent.")
                    
                elif task == "0":
                    break
                else:
                    print("Invalid input")
                    
        if name in beginners:
            admin = AdminFactory.buildAdmin(0)
            print("You can send requests for help.")
            while True:
                print()
                task = input("Press s to send a help request to the admin.\nPress 0 for exit  ")
                
                if task == "s":
                    request1 = input("What need help with: ")
                    message = (name + " request help.\n" + request1)
                    admin.sendRequests(str(message))
                    print("Request sent.")
                elif task == "0":
                    break
                else:
                    print("Invalid input")  
        
        else:
            print("Sorry, no accces for you")
            print()
    
    else:
        print("Invalid choice.")
        print()
              
                

            

