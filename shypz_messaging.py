import pika
from model.User_OTP import User_OTP
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='shypz_otp')

user_otp = User_OTP('9739325635','Welcome to shypz your otp is 123456')

user_otp_message = {'mobile':user_otp.getMobile(),'message':user_otp.getMessage()}


#for i in range(10):

channel.basic_publish(exchange='',
                      routing_key='shypz_otp',
                      body=json.dumps(user_otp_message))

print(" [x] Sent OTP message")

connection.close()