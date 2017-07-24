import urllib # Python URL functions
import urllib2 # Python URL functions

authkey = "163033AqvqrX8JkqG559537d59" # Your authentication key.

mobiles = "9739325635" # Multiple mobiles numbers separated by comma.

message = "your opt is 123456" # Your message to send.

sender = "ShypzL" # Sender ID,While using route4 sender id should be 6 characters long.

route = "4" # Define route

# Prepare you post parameters
values = {
          'authkey' : authkey,
          'mobiles' : mobiles,
          'message' : message,
          'sender' : sender,
          'route' : route
          }


url = "https://control.msg91.com/api/sendhttp.php" # API URL

print values

#postdata = urllib.urlencode(values) # URL encoding the data here.

#req = urllib2.Request(url, postdata)

#response = urllib2.urlopen(req)

#output = response.read() # Get Response

#print output # Print Response