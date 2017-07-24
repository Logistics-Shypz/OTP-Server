import pika
import json
from loggingShypz_logger.ShypzLogger import ShypzLogger
from model.User_OTP import User_OTP

shypzlogger = ShypzLogger().getShypzLogger()

class ShypzSender:
    
    
    
    def __init__(self,otp_obj):
        self.otp_obj = otp_obj
        
    def send_message(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
    
        channel.queue_declare(queue='shypz_otp')
        mobile = self.otp_obj.getMobile()
        message = self.otp_obj.getMessage()
        user_otp_message = {'mobile':mobile,'message':message}
        channel.basic_publish(exchange='',
                          routing_key='shypz_otp',
                          body=json.dumps(user_otp_message))
        shypzlogger.info("Sent Message " + str(user_otp_message) + "to Queue shypz_otp")
        connection.close()
        