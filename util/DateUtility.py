import datetime

def getTime():
	current_time = datetime.datetime.now()
	return current_time

def getStrFTime():
	current_time = datetime.datetime.now()
	return current_time.strftime("%Y-%m-%d %H:%M")



	