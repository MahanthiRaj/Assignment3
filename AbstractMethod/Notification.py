from abc import ABC, abstractmethod

class Notification:
    
    @abstractmethod
    def send(self):
        pass
    
    @abstractmethod
    def log(self):
        pass
    
class SMSnotification(Notification):
    def send(self):
        return "sms sent"
    
    
    def log(self):
        return "sms log"
class EmailNotifocation(Notification):
    
    def send(self):
        return "Email sent"
    
    def log(self):
        return "Email log"
    
s = SMSnotification()
e = EmailNotifocation()

print(s.send())
print(s.log())
print(e.send())
print(e.log())