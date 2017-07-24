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


app = Flask(__name__)
#app.response_class = ShypzResponse
app.secret_key = 'shypz_secret'

url='http://localhost:5000/'

msg91portal_url = "https://control.msg91.com/api/sendhttp.php"

smsutil = SMSUtil()

shypzlogger = ShypzLogger().getShypzLogger()

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
	return render_template('registration.html')
		
		
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
		
		user_res = requests.post('http://localhost:8080/users',json=user_payload)
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
			user_get_res = requests.get('http://localhost:8080/users/name/' + _username)
			user_json = user_get_res.json()
			user_id = user_json['User']['id']
			user_otp_url = "http://localhost:8080/users/id/" + str(user_id) + "/otp"
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
		return render_template('registration.html')
	
	
	
@app.route('/login',methods=['POST','GET'])
def signin():
	return render_template('login.html')


@app.route('/dologin',methods=['POST'])
def do_login():
	_username = request.form['nm']
	_userpwd = request.form['pass']
	user_payload = {"username" : _username,"user_Password" : _userpwd}
	user_get_res = requests.get('http://localhost:8080/users/name/' + _username)
	user_json = user_get_res.json()
	if user_json['User'] is None:
		return render_template('login.html')
	else:
		user_id = user_json['User']['id']
		user_name = user_json['User']['username']
		session['username'] = user_name
		return render_template('index.html',username=session['username'])
	


@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('index'))


@app.route('/verifyotp',methods=['POST'])
def verifyOTP():
	otp = request.form['otp']
	user_otp_payload={"userotp" : otp,"userverification" : 1}
	_username = session['username']
	user_get_res = requests.get('http://localhost:8080/users/name/' + _username)
	user_json = user_get_res.json()
	user_id = user_json['User']['id']
	user_otp_url = "http://localhost:8080/users/id/" + str(user_id) + "/otp"
	user_otp_res = requests.put(user_otp_url, json=user_otp_payload)
	return redirect(url_for('index'))


@app.route('/otp/<mobile>',methods=['GET'])
def genOTP(mobile):
	otp1 = OTP()
	ot = otp1.generateOTP_v2(mobile)
	otp_response = {'otp':ot,'success_flag':'1'}
	#shypz_response = ShypzResponse(status=ResponseCodes.SUCCESS.value,data=ot,mimetype='application/json',content_type='application/json')
	return jsonify(otp_response)

if __name__ == '__main__':
	app.run('0.0.0.0',port=5000,debug=True,threaded=True)