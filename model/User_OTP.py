class User_OTP:
    def __init__(self,mobile,message):
        self.mobile = mobile
        self.message = message
        
    def getMobile(self):
        return self.mobile
    
    def getMessage(self):
        return self.message
    
    def setMobile(self,mobile):
        self.mobile = mobile
        
    def setMessage(self,message):
        self.message= message