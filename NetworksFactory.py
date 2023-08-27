#Create and abstract class called NetDevice, with abstract methods powerUp() and shutdown().
#Create three child network device classes.
#Create a factory that will return a specific network device based on the user input
from abc import ABC, abstractmethod

class NetDevice:
    @staticmethod
    def powerUP(self):
        pass
    def shutdown(self):
        pass
        
class CiscoSwitch:
    def powerUP(self):
        print('Cisco is powering up, BEEP BEEP')
    def shutdown(self):
        print('Cisco is tired, time for sleep.')
    def configure(self):
        print("You can now configure the main Router.")
        
class Repeater:
    def powerUP(self):
        print('WiFi range is now longer than ever.')
    def shutdown(self):
        print('WiFi range returned to default.')
        
class SecurityHUB:
    def powerUP(self):
        print('Security hub is up and running.')
    def shutdown(self):
        print('Alert, security down, I repeat ....')
        
class NetworkFactory:
    @staticmethod
    def networkstatus(device):
        if device == 'ciscoswitch':
            return CiscoSwitch()
        if device == 'repeater':
            return Repeater()
        if device == 'securityhub':
            return SecurityHUB()

if __name__ == "__main__":
    choice = input('Please enter the device you want to manage: ')
    device = NetworkFactory.networkstatus(choice)
    device.powerUP()
    device.shutdown()
        

    