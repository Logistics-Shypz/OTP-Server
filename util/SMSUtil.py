import ConfigParser
import os
import settings

templates_dir = os.path.join(os.path.dirname(settings.__file__))
template_file = os.path.join(templates_dir, 'sms_settings.cfg')

class SMSUtil:
    
    url = ""
    authkey = ""
    sender = ""
    route = ""
    
    def createPostParameters(self,mobile,message):
        config = ConfigParser.ConfigParser()
        try:
            print "i am in try"
            config.read(template_file)
            print config
        except:
            print "unable to read file"
        values = {
                'authkey' : config.get('Keys','authkey'),
                'mobiles' : mobile,
                'message' : message,
                'sender' : config.get('Keys','sender'),
                'route' : config.get('Keys','route')
            
            
            }
        
        return values
    
    
    
    
#smsutil = SMSUtil()

#print "test"

#values = smsutil.createPostParameters('9739325635', "hello world")

#print values


        
        
        
        
    