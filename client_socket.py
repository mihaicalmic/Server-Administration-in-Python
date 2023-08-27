import socket
import subprocess

class Client:
    
    def request(self,url):
        HOST = 'localhost'
        PORT = 7777
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            word1 = (url.encode())
            s.sendall(word1)
            data = s.recv(1024).decode()

        return data
    
    def dnsrequest(url):
        subprocess.Popen(["python", "server_socket.py"])
        client = Client()
        ip = client.request(url)
        print(ip)


#Client.dnsrequest("192.168.1.8")
