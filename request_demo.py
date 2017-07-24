import requests
from util import DateUtility as du
start_time = du.getTime()
payload={'mobile':'98'}
r = requests.get('http://localhost:5000/otp/98')
print r.text
end_time = du.getTime()

print "the time took is %s " %(end_time-start_time)