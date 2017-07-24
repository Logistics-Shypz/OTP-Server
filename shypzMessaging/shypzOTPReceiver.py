import pika
import json as json
from json import loads
from loggingShypz_logger.ShypzLogger import ShypzLogger
from model.User_OTP import User_OTP
import urllib
import urllib2
from util.SMSUtil import SMSUtil

shypzlogger = ShypzLogger().getShypzLogger()

msg91portal_url = "https://control.msg91.com/api/sendhttp.php"

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.queue_declare(queue='shypz_otp')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    user_otp = loads(body)
    smsutil = SMSUtil()
    values = smsutil.createPostParameters(user_otp['mobile'],user_otp['message'])
    print values
    """postdata = urllib.urlencode(values)
    req = urllib2.Request(msg91portal_url, postdata)
    response = urllib2.urlopen(req)
    output = response.read()"""
    output = "sent"
    shypzlogger.info("Message sent to User mobile " + user_otp['mobile'] + " with output" + output)
    
channel.basic_consume(callback,
                      queue='shypz_otp',
                      no_ack=True)

shypzlogger.info(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()