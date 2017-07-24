import ConfigParser
from util.SMSUtil import SMSUtil
import settings
import os

smsutil = SMSUtil()

values = smsutil.createPostParameters('9739325635', 'hello')
print values
