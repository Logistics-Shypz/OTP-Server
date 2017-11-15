from flask import Flask,redirect,url_for,Request,request,Response
from flask import make_response
from util.OTP import OTP
from util.SMSUtil import SMSUtil
from flask.templating import render_template
from flask.globals import session
import requests
from util import DateUtility as du
from sympy.utilities.decorator import threaded
import urllib
import urllib2
from loggingShypz_logger.ShypzLogger import ShypzLogger
import logging
import json
from flask import jsonify
from shypzResponse.shypzResponse import ShypzResponse
from shypzResponse.ResponseCodes import ResponseCodes
from django.contrib.messages.api import success
import pika
from model.User_OTP import User_OTP
from shypzMessaging.shypzSender import ShypzSender
import googlemaps
from datetime import datetime
from nltk.metrics import distance



app = Flask(__name__)

print app
#app.response_class = ShypzResponse
app.secret_key = 'shypz_secret'

approot = '/api/'

url='http://localhost:5000/'

backendserverurl = 'http://localhost:8080'

booking_backendserver_url = 'http://localhost:8083'
booking_approot = '/api/v1/'

msg91portal_url = "https://control.msg91.com/api/sendhttp.php"

smsutil = SMSUtil()

shypzlogger = ShypzLogger().getShypzLogger()

gmaps = googlemaps.Client(key='AIzaSyCV-p2cQJYytd8L-b4Gen2gvYrJg5xA4w8')

"""
@app.route('/shypz',methods=['GET','POST'])
def indextest():
	return render_template('ui/index.html',username="guest")

@app.route('/landing',methods=['GET','POST'])
def landingtest():
	return render_template('static/partials/landing.html',username="guest")

"""
@app.route('/')
def index():
	
	ls = [1,2,3,4,5]
	ret_data = {'status':200,'message':'success','text':ls}
	my_resp = make_response('Response')
	my_resp.headers['test'] = '34'
	my_resp.data = json.dumps(ret_data)
	my_resp.mimetype = 	'application/json'
	shypzlogger.info('Received request for index')

	if 'username' in session:
		username = session['username']
		#return 'Logged in as ' + username + '<br>' + \
        #"<b><a href = '/logout'>click here to log out</a></b>"
		return render_template('index.html',username=username)
	shypzlogger.info('username is null setting to guest')
	
	mess = "test"
	return render_template('index.html',username="guest")
	#return my_resp


@app.route('/signup',methods=['GET','POST'])
def signup():
	shypzlogger.info('Received request for signup')
	if request.method == 'POST':
		print "method POST"
	else:
		print "method GET"
	return render_template('registration.html',username="guest")
		
		
@app.route('/register',methods=['GET','POST'])
def formdata():
	if request.method == "POST":
		
		print "in Register post method"
		_username = request.form['nm']
		_user_mobile = request.form['mob']
		_userpwd = request.form['pwd']
		_useremail = request.form['email']
		
		#otp = OTP()
		#ot = otp.generateOTP_v2(_user_mobile)
		#print ot
		#url_cons = url+"otp/"+_user_mobile
		
		
		
		user_payload = {"username" : _username,"userEmail" : _useremail,"user_Password" : _userpwd,"user_Mobile" : _user_mobile}
		
		serv_address_user_service = backendserverurl + approot + 'users'
		user_res = requests.post(serv_address_user_service,json=user_payload)
		print user_res.json()
		user_json_res = user_res.json()
		success_code = user_json_res['success_code']
		if success_code == 1:
			start_time = du.getTime()
			session['username'] = _username
			res_otp = requests.get('http://localhost:5000/otp/'+_user_mobile)
			res_otp_json = res_otp.json()
			print res_otp_json
			otp = res_otp_json['otp']
			end_time = du.getTime()
			#print end_time
			print "the time took is %s " %(end_time-start_time)
			user_otp_payload={"userotp" : otp,"userverification" : 0}
			serv_address_user_service_with_name = backendserverurl + approot + 'users/name/'
			user_get_res = requests.get(serv_address_user_service_with_name + _username)
			user_json = user_get_res.json()
			user_id = user_json['User']['id']
			serv_otp_user_service_with_id = backendserverurl + approot + 'users/id/'
			user_otp_url = serv_otp_user_service_with_id + str(user_id) + "/otp"
			user_otp_res = requests.post(user_otp_url,json=user_otp_payload)
			#print user_otp_res.text
			message = "Welcome " + _username +  " to Shypz your OTP is %s " %(otp)
			print message
			user_otp = User_OTP(_user_mobile,message)
			
			sender = ShypzSender(user_otp)
			sender.send_message()
			"""values = smsutil.createPostParameters(_user_mobile,message)
			print values
			postdata = urllib.urlencode(values)
			req = urllib2.Request(msg91portal_url, postdata)
			response = urllib2.urlopen(req)
			output = response.read() 
			print output
			"""
			
			return render_template('otp_verification.html',username=_username)
		elif success_code == 2:
			print user_json_res['message']
			return render_template('login.html')
	else:
		return render_template('registration.html',username="guest")
	
	
	
@app.route('/login',methods=['POST','GET'])
def signin():
	return render_template('login.html')


@app.route('/dologin',methods=['POST'])
def do_login():
	_username = request.form['nm']
	_userpwd = request.form['pass']
	user_payload = {"username" : _username,"user_Password" : _userpwd}
	serv_user_login_service = backendserverurl + approot + 'users/name/'
	user_get_res = requests.get(serv_user_login_service + _username)
	user_json = user_get_res.json()
	if user_json['User'] is None:
		return render_template('login.html')
	else:
		user_id = user_json['User']['id']
		user_name = user_json['User']['username']
		session['username'] = user_name
		return render_template('UserDashboard.html',username=session['username'])


@app.route('/useraccount')
def account():
	#print session['username']
	return render_template('UserDashboard.html',username=session['username'])

#api to track user booking history
@app.route('/userbookings')
def bookings():
	#print session['username']
	return render_template('Bookings.html',username=session['username'])


@app.route('/orderbooking',methods=['POST','GET'])
def order_booking():
	print "in order bookingaction form"
	if 'username' in session:
		return render_template('mainActions.html',username=session['username'])
	else:
		return render_template('mainActions.html',username="guest")

#api to show user booking form
@app.route('/userbookingform',methods=['POST','GET'])
def booking_form():
	print "In booking_form"
	#option_value = request.form['options']
	#print option_value;
	if 'username' in session:
		return render_template('order-begin.html',username=session['username'])
	else:
		return render_template('order-begin.html',username="guest")
	
@app.route('/bookinguserform')	
def booking_userform():
	if 'username' in session:
		return render_template('booking-form.html',username=session['username'])
	else:
		return render_template('booking-form.html',username="guest")
	
	
@app.route('/bookinguserinfo')	
def booking_userinfo():
	if 'username' in session:
		return render_template('booking-userinfo.html',username=session['username'])
	else:
		return render_template('booking-userinfo.html',username="guest")
	
	
@app.route('/bookinguseritems')	
def booking_items():
	if 'username' in session:
		return render_template('booking-items.html',username=session['username'])
	else:
		return render_template('booking-items.html',username="guest")
	
	
@app.route('/bookinguseraddress')	
def booking_address():
	if 'username' in session:
		return render_template('booking-address.html',username=session['username'])
	else:
		return render_template('booking-address.html',username="guest")
	
	
@app.route('/orderarticle')	
def order_article():
	print "in order article"
	if 'username' in session:
		return render_template('order-article.html',username=session['username'])
	else:
		return render_template('order-article.html',username="guest")
		
	#print request.form['options']

@app.route('/ordercontact')	
def order_contact():
	print "in order article"
	if 'username' in session:
		return render_template('order-contact.html',username=session['username'])
	else:
		return render_template('order-contact.html',username="guest")	


@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('index'))


@app.route('/Address')
def address():
	print "In Address request user app"
	return render_template('Address.html',username=session['username'])

@app.route('/updateAddress',methods=['POST'])
def updateProfileAddress():
	address_json = json.loads(request.data)
	#print address_json
	serv_user_address_service = backendserverurl + approot + 'users/name/' + address_json['username'] + '/address'
	user_get_res = requests.get(serv_user_address_service)
	user_address_json_response = user_get_res.json()
	#print user_address_json_response[0]['addressId']
	#print type(user_address_json_response['addressId'])
	
	if len(user_get_res.json()) == 1:
		serv_post_address_service = backendserverurl + approot + 'users/name/' + address_json['username'] + '/address/' + str(user_address_json_response[0]['addressId'])
		user_address_res = requests.put(serv_post_address_service,json=address_json)
		print user_address_res.json()
		return json.dumps(user_address_res.json())
	else:
		serv_post_address_service = backendserverurl + approot + 'users/name/' + address_json['username'] + '/address'
		user_address_res = requests.post(serv_post_address_service,json=address_json)
		print user_address_res.json()
		return json.dumps(user_address_res.json())


@app.route('/Contact')
def contact():
	return render_template('Contact.html',username=session['username'])

@app.route('/Password')
def password():
	return render_template('Password.html',username=session['username'])

@app.route('/Promotions')
def promotions():
	return render_template('Promotions.html',username=session['username'])





@app.route('/verifyotp',methods=['POST'])
def verifyOTP():
	otp = request.form['otp']
	user_otp_payload={"userotp" : otp,"userverification" : 1}
	print user_otp_payload
	_username = session['username']
	print _username
	serv_verify_otp_service = backendserverurl + approot + 'users/name/'
	print serv_verify_otp_service
	user_get_res = requests.get(serv_verify_otp_service + _username)
	print user_get_res
	user_json = user_get_res.json()
	user_id = user_json['User']['id']
	serv_put_otp_service = backendserverurl + approot + 'users/id/'
	user_otp_url = serv_put_otp_service + str(user_id) + "/otp"
	print user_otp_url
	user_otp_res = requests.put(user_otp_url, json=user_otp_payload)
	return redirect(url_for('index'))


@app.route('/otp/<mobile>',methods=['GET'])
def genOTP(mobile):
	otp1 = OTP()
	ot = otp1.generateOTP_v2(mobile)
	otp_response = {'otp':ot,'success_flag':'1'}
	#shypz_response = ShypzResponse(status=ResponseCodes.SUCCESS.value,data=ot,mimetype='application/json',content_type='application/json')
	return jsonify(otp_response)

@app.route('/server/session',methods=['GET'])
def getServerSession():
	if 'username' in session:
		username = session['username']
		return username
	else:
		username = "guest"
		return username
	
@app.route('/orderSummary',methods=['GET'])	
def order_summary():
	if 'username' in session:
		return render_template('OrderSummary.html',username=session['username'])
	else:
		return render_template('OrderSummary.html',username="guest")
	
@app.route('/orderBook',methods=['POST'])		
def order_book():
	print "In order book"
	final_order_json = json.loads(request.data)
	print final_order_json;
	#print final_order_json
	serv_post_booking_service = booking_backendserver_url + booking_approot + 'bookings'
	booking_res = requests.post(serv_post_booking_service,json=final_order_json)
	booking_json_response = booking_res.json()
	return jsonify(booking_json_response)

@app.route('/gmap')
def getMap():
	return render_template('google_nav_example.html')


@app.route('/showBookingNav',methods=['GET'])
def showBookingNavPage():
	origin = request.args.get('from')
	destination = request.args.get('to')
	
	print origin;
	print destination;
	if 'username' in session:
		return render_template('booking-nav.html',username=session['username'],origins=origin,destinations=destination)
	else:
		return render_template('booking-nav.html',username="guest",origins=origin,destinations=destination)

@app.route('/getDistance',methods=['GET','POST'])
def getDistance():
	print "In get distance"
	
	loc = json.loads(request.data)
	
	
	origin = loc['from']
	destination = loc['to']
	
	res = gmaps.distance_matrix(origin,destination)
	
	
	
	distance_response = {}
	if res['status'] == "OK":
		distance_response['distance'] = res['rows'][0]['elements'][0]['distance']['text']
		distance_response['time'] = res['rows'][0]['elements'][0]['duration']['text']
		distance_response['origin'] = origin
		distance_response['destination'] = destination
	
	
	return jsonify(distance_response)
	



if __name__ == '__main__':
	app.run('0.0.0.0',port=5000,debug=True,threaded=True)