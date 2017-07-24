import pika
import json
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.queue_declare(queue='shypz_otp')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % json.dumps(body))
    
channel.basic_consume(callback,
                      queue='shypz_otp',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()