import os
import sys
import json
import logging
import logging.config

class ShypzLogger():
	def __init__(self):
		try:
			my_path = os.path.abspath(os.path.dirname(__file__))
			path = os.path.join(my_path, "..\loggingShypz_config\logging_properties.json")
			final_config=""

			if os.path.exists(path): 
				with open(path, 'rt') as f:
					config = json.load(f)

				final_config = config
			logging.config.dictConfig(config)
			print final_config
			self._shypzlogger = logging.getLogger('ShypzCustomLogger')
			

		except Exception as ex:
			logging.error("An error occurred while creating a log entry using log4SShypz............. " + str(ex))


	def getShypzLogger(self):
		try:
			return self._shypzlogger
		except Exception as ex:
			logging.error("Log4Shypz _logger is not initialized due to an exception....... " + str(ex))
			return None


