
from loggingShypz_logger.ShypzLogger import ShypzLogger
import logging


"""
my_path = os.path.abspath(os.path.dirname(__file__))



path = os.path.join(my_path, "loggingShypz_config\logging_properties.json")


final_config=""

if os.path.exists(path): 
	with open(path, 'rt') as f:
		config = json.load(f)

	final_config = config

print final_config

logging.config.dictConfig(config)

"""


#logger = logging.getLogger('ShypzCustomLogger')

shypzlogger = ShypzLogger().getShypzLogger()


def hello(st):
	shypzlogger.info('Received %s in hello()',(st))
	return "hello " + st


a = hello("anubhav")


"""
logging.basicConfig(filename='example.log',format='%(asctime)s:%(pathname)s:%(filename)s:%(levelname)s:%(module)s:%(funcName)s:%(lineno)d:%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)

loglevel=""
for arg in sys.argv:
	if arg.startswith('--'):
		k,v = arg.split("=")
		loglevel = v

print loglevel

print getattr(logging, loglevel.upper())

def hello(st):
	logging.info('Received %s in hello()',(st))
	return "hello " + st


a = hello("anubhav")

"""
